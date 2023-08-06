import json
import logging
import logging.config
import os
import sys
import re
import requests
import yaml
import atexit
import ert.shared
from argparse import ArgumentParser, ArgumentTypeError
from contextlib import contextmanager
from ert.logging._log_util_abort import _log_util_abort
from ecl import set_abort_handler
from ert.logging import LOGGING_CONFIG
from ert.shared.cli.main import run_cli, ErtCliError
from ert.shared.cli import (
    ENSEMBLE_SMOOTHER_MODE,
    ENSEMBLE_EXPERIMENT_MODE,
    ITERATIVE_ENSEMBLE_SMOOTHER_MODE,
    ES_MDA_MODE,
    TEST_RUN_MODE,
    WORKFLOW_MODE,
)
from ert.shared.ide.keywords.definitions import (
    RangeStringArgument,
    ProperNameArgument,
    ProperNameFormatArgument,
    NumberListStringArgument,
    IntegerArgument,
)
from ert.shared.models.multiple_data_assimilation import MultipleDataAssimilation
from ert.shared.plugins.plugin_manager import ErtPluginContext
from ert.shared.feature_toggling import FeatureToggling
from ert.shared.storage.command import add_parser_options as ert_api_add_parser_options
from ert.shared.services import Storage, WebvizErt


def run_ert_storage(args):
    kwargs = {"res_config": args.config}
    kwargs["verbose"] = True

    if args.database_url is not None:
        kwargs["database_url"] = args.database_url

    with Storage.start_server(**kwargs) as server:
        server.wait()


def run_webviz_ert(args):
    try:
        import webviz_ert  # noqa
    except ImportError as err:
        raise ValueError(
            "Running `ert vis` requires that webviz_ert is installed"
        ) from err
    kwargs = {"res_config": args.config}
    kwargs["verbose"] = args.verbose

    if args.database_url is not None:
        kwargs["database_url"] = args.database_url

    with Storage.connect_or_start_server(**kwargs) as storage:
        storage.wait_until_ready()
        url = storage.fetch_url()
        auth = storage.fetch_auth()
        response = requests.get(f"{url}/server/info", headers={"Token": auth[1]})
        if response.status_code == 200:
            title = json.loads(response.content)["name"]
        else:
            title = "ERT - Visualization tool"
        print(
            """
-----------------------------------------------------------

Starting up Webviz-ERT. This might take more than a minute.

-----------------------------------------------------------
"""
        )
        kwargs = {
            "experimental_mode": args.experimental_mode,
            "verbose": args.verbose,
            "title": title,
        }
        with WebvizErt.start_server(**kwargs) as webviz_ert_server:
            webviz_ert_server.wait()


def strip_error_message_and_raise_exception(validated):
    error = validated.message()
    error = re.sub(r"\<[^>]*\>", " ", error)
    raise ArgumentTypeError(error)


def valid_file(fname):
    if not os.path.isfile(fname):
        raise ArgumentTypeError(f"File was not found: {fname}")
    return fname


def valid_realizations(user_input):
    validator = RangeStringArgument()
    validated = validator.validate(user_input)
    if validated.failed():
        strip_error_message_and_raise_exception(validated)
    return user_input


def valid_weights(user_input):
    validator = NumberListStringArgument()
    validated = validator.validate(user_input)
    if validated.failed():
        strip_error_message_and_raise_exception(validated)
    return user_input


def valid_name_format(user_input):
    validator = ProperNameFormatArgument()
    validated = validator.validate(user_input)
    if validated.failed():
        strip_error_message_and_raise_exception(validated)
    return user_input


def valid_name(user_input):
    validator = ProperNameArgument()
    validated = validator.validate(user_input)
    if validated.failed():
        strip_error_message_and_raise_exception(validated)
    return user_input


def valid_iter_num(user_input):
    validator = IntegerArgument(from_value=0)
    validated = validator.validate(user_input)
    if validated.failed():
        strip_error_message_and_raise_exception(validated)
    return user_input


def valid_num_iterations(user_input):
    validator = IntegerArgument(from_value=1)
    validated = validator.validate(user_input)
    if validated.failed():
        strip_error_message_and_raise_exception(validated)
    return user_input


def attemp_int_conversion(val: str) -> int:
    try:
        return int(val)
    except ValueError:
        raise ArgumentTypeError(f"{val} is not a valid integer")


def convert_port(val: str) -> int:
    val = attemp_int_conversion(val)
    if not (0 <= val <= 65535):
        raise ArgumentTypeError(f"{val} is not in valid port range 0-65535")
    return val


def valid_port_range(user_input: str) -> range:
    if "-" not in user_input:
        raise ArgumentTypeError("Port range must contain two integers separated by '-'")
    a, b = user_input.split("-")

    a, b = convert_port(a), convert_port(b)

    if b < a:
        raise ArgumentTypeError(f"Invalid port range [{a},{b}], {b} is < {a}")

    return range(a, b + 1)


def range_limited_int(user_input):
    try:
        i = int(user_input)
    except ValueError:
        raise ArgumentTypeError("Must be a int")
    if 0 < i < 100:
        return i
    raise ArgumentTypeError("Range must be in range 1 - 99")


def run_gui_wrapper(args):
    from ert.gui.gert_main import run_gui

    run_gui(args)


def get_ert_parser(parser=None):
    if parser is None:
        parser = ArgumentParser(description="ERT - Ensemble Reservoir Tool")

    parser.add_argument(
        "--version",
        action="version",
        version=f"{ert.shared.__version__}",
    )

    parser.add_argument(
        "--logdir",
        required=False,
        type=str,
        default="./logs",
        help="Directory where ERT will store the logs. Default is ./logs",
    )

    subparsers = parser.add_subparsers(
        title="Available user entries",
        description="ERT can be accessed through a GUI or CLI interface. Include "
        "one of the following arguments to change between the "
        "interfaces. Note that different sub commands may require "
        "different additional arguments. See the help section for "
        "each sub command for more details.",
        help="Available sub commands",
        dest="mode",
    )
    subparsers.required = True

    config_help = "ERT configuration file"

    # gui_parser
    gui_parser = subparsers.add_parser(
        "gui",
        description="Opens an independent graphical user interface for "
        "the user to interact with ERT.",
    )
    gui_parser.set_defaults(func=run_gui_wrapper)
    gui_parser.add_argument("config", type=valid_file, help=config_help)
    gui_parser.add_argument(
        "--verbose", action="store_true", help="Show verbose output.", default=False
    )
    FeatureToggling.add_feature_toggling_args(gui_parser)

    # ert_api
    ert_api_parser = subparsers.add_parser(
        "api",
        description="Expose ERT data through an HTTP server",
    )
    ert_api_parser.set_defaults(func=run_ert_storage)
    ert_api_add_parser_options(ert_api_parser)

    ert_vis_parser = subparsers.add_parser(
        "vis",
        description="Launch webviz-driven visualization tool.",
    )
    ert_vis_parser.set_defaults(func=run_webviz_ert)
    ert_vis_parser.add_argument("--name", "-n", type=str, default="Webviz-ERT")
    ert_vis_parser.add_argument(
        "--experimental-mode",
        action="store_true",
        help="Feature flag for enabling experimental plugins",
    )
    ert_api_add_parser_options(ert_vis_parser)  # ert vis shares args with ert api

    # test_run_parser
    test_run_description = f"Run '{TEST_RUN_MODE}' in cli"
    test_run_parser = subparsers.add_parser(
        TEST_RUN_MODE, help=test_run_description, description=test_run_description
    )

    # ensemble_experiment_parser
    ensemble_experiment_description = (
        "Run simulations in cli without performing any updates on the parameters."
    )
    ensemble_experiment_parser = subparsers.add_parser(
        ENSEMBLE_EXPERIMENT_MODE,
        description=ensemble_experiment_description,
        help=ensemble_experiment_description,
    )
    ensemble_experiment_parser.add_argument(
        "--realizations",
        type=valid_realizations,
        help="These are the realizations that will be used to perform simulations. "
        "For example, if 'Number of realizations:50 and Active realizations is 0-9', "
        "then only realizations 0,1,2,3,...,9 will be used to perform simulations "
        "while realizations 10,11, 12,...,49 will be excluded.",
    )
    ensemble_experiment_parser.add_argument(
        "--current-case",
        type=valid_name,
        required=False,
        help="Name of the case where the results for the simulation "
        "using the prior parameters will be stored.",
    )

    ensemble_experiment_parser.add_argument(
        "--iter-num",
        type=valid_iter_num,
        default=0,
        required=False,
        help="Specification of which iteration number is about to be made. "
        "Use iter-num to avoid recomputing the priors.",
    )

    # ensemble_smoother_parser
    ensemble_smoother_description = (
        "Run simulations in cli while performing one update"
        " on the parameters by using the ensemble smoother algorithm."
    )
    ensemble_smoother_parser = subparsers.add_parser(
        ENSEMBLE_SMOOTHER_MODE,
        description=ensemble_smoother_description,
        help=ensemble_smoother_description,
    )
    ensemble_smoother_parser.add_argument(
        "--target-case",
        type=valid_name,
        required=True,
        help="Name of the case where the results for the "
        "updated parameters will be stored.",
    )
    ensemble_smoother_parser.add_argument(
        "--realizations",
        type=valid_realizations,
        help="These are the realizations that will be used to perform simulations."
        "For example, if 'Number of realizations:50 and Active realizations is 0-9', "
        "then only realizations 0,1,2,3,...,9 will be used to perform simulations "
        "while realizations 10,11, 12,...,49 will be excluded",
    )
    ensemble_smoother_parser.add_argument(
        "--current-case",
        type=valid_name,
        required=False,
        help="Name of the case where the results for the simulation "
        "using the prior parameters will be stored.",
    )

    # iterative_ensemble_smoother_parser
    iterative_ensemble_smoother_description = (
        "Run simulations in cli while performing updates"
        " on the parameters using the iterative ensemble smoother algorithm."
    )
    iterative_ensemble_smoother_parser = subparsers.add_parser(
        ITERATIVE_ENSEMBLE_SMOOTHER_MODE,
        description=iterative_ensemble_smoother_description,
        help=iterative_ensemble_smoother_description,
    )
    iterative_ensemble_smoother_parser.add_argument(
        "--target-case",
        type=valid_name_format,
        required=True,
        help="The iterative ensemble smoother creates multiple cases for the different "
        "iterations. The case names will follow the specified format. "
        "For example, 'Target case format: iter_%%d' will generate "
        "cases with the names iter_0, iter_1, iter_2, iter_3, ....",
    )
    iterative_ensemble_smoother_parser.add_argument(
        "--realizations",
        type=valid_realizations,
        help="These are the realizations that will be used to perform simulations."
        "For example, if 'Number of realizations:50 and active realizations are 0-9', "
        "then only realizations 0,1,2,3,...,9 will be used to perform simulations "
        "while realizations 10,11, 12,...,49 will be excluded.",
    )
    iterative_ensemble_smoother_parser.add_argument(
        "--current-case",
        type=valid_name,
        required=False,
        help="Name of the case where the results for the simulation "
        "using the prior parameters will be stored.",
    )
    iterative_ensemble_smoother_parser.add_argument(
        "--num-iterations",
        type=valid_num_iterations,
        required=False,
        help="The number of iterations to run.",
    )

    # es_mda_parser
    es_mda_description = f"Run '{ES_MDA_MODE}' in cli"
    es_mda_parser = subparsers.add_parser(
        ES_MDA_MODE, description=es_mda_description, help=es_mda_description
    )
    es_mda_parser.add_argument(
        "--target-case",
        type=valid_name_format,
        help="The es_mda creates multiple cases for the different "
        "iterations. The case names will follow the specified format. "
        "For example, 'Target case format: iter-%%d' will generate "
        "cases with the names iter-0, iter-1, iter-2, iter-3, ....",
    )
    es_mda_parser.add_argument(
        "--realizations",
        type=valid_realizations,
        help="These are the realizations that will be used to perform simulations."
        "For example, if 'Number of realizations:50 and active realizations are 0-9', "
        "then only realizations 0,1,2,3,...,9 will be used to perform simulations "
        "while realizations 10,11, 12,...,49 will be excluded.",
    )
    es_mda_parser.add_argument(
        "--weights",
        type=valid_weights,
        default=MultipleDataAssimilation.default_weights,
        help="Example custom relative weights: '8,4,2,1'. This means multiple data "
        "assimilation ensemble smoother will half the weight applied to the "
        "observation errors from one iteration to the next across 4 iterations.",
    )
    es_mda_parser.add_argument(
        "--current-case",
        type=valid_name,
        required=False,
        help="Name of the case where the results for the simulation "
        "using the prior parameters will be stored.",
    )
    es_mda_parser.add_argument(
        "--start-iteration",
        default="0",
        type=valid_iter_num,
        required=False,
        help="Which iteration the evaluation should start from. "
        "Requires cases previous to the specified iteration to exist.",
    )

    workflow_description = "Executes the workflow given"
    workflow_parser = subparsers.add_parser(
        WORKFLOW_MODE, help=workflow_description, description=workflow_description
    )
    workflow_parser.add_argument(help="Name of workflow", dest="name")

    # Common arguments/defaults for all non-gui modes
    for cli_parser in [
        test_run_parser,
        ensemble_experiment_parser,
        ensemble_smoother_parser,
        iterative_ensemble_smoother_parser,
        es_mda_parser,
        workflow_parser,
    ]:
        cli_parser.set_defaults(func=run_cli)
        cli_parser.add_argument(
            "--verbose", action="store_true", help="Show verbose output.", default=False
        )
        cli_parser.add_argument(
            "--color-always",
            action="store_true",
            help="Force coloring of monitor output, which is automatically"
            + " disabled if the output stream is not a terminal.",
            default=False,
        )
        cli_parser.add_argument(
            "--disable-monitoring",
            action="store_true",
            help="Disable monitoring.",
            default=False,
        )
        cli_parser.add_argument(
            "--port-range",
            type=valid_port_range,
            required=False,
            help="Port range [a,b] to be used by the evaluator. Format: a-b",
        )
        cli_parser.add_argument("config", type=valid_file, help=config_help)

        FeatureToggling.add_feature_toggling_args(cli_parser)

    return parser


def ert_parser(parser, argv):
    return get_ert_parser(parser).parse_args(argv)


@contextmanager
def start_ert_server(mode: str):
    if mode in ("api", "vis") or not FeatureToggling.is_enabled("new-storage"):
        yield
        return

    with Storage.start_server():
        yield


def log_config(config_path: str, logger: logging.Logger) -> None:
    """
    Logs what configuration was used to start ert. Because the config
    parsing is quite convoluted we are not able to remove all the comments,
    but the easy ones are filtered out.
    """
    if config_path is not None and os.path.isfile(config_path):
        config_context = ""
        with open(config_path, "r", encoding="utf-8") as file_obj:
            for line in file_obj:
                line = line.strip()
                if not line or line.startswith("--"):
                    continue
                if "--" in line:
                    # There might be a comment in this line, but it could
                    # also be an argument to a job, so we do a quick check
                    if not any(x in line for x in ['"', "'"]):
                        line = line.split("--")[0].rstrip()
                config_context += line + "\n"
        logger.info(
            f"Content of the configuration file ({config_path}):\n" + config_context
        )


@atexit.register
def log_process_usage():
    try:
        import resource

        usage = resource.getrusage(resource.RUSAGE_SELF)

        if sys.platform == "darwin":
            # macOS apparently outputs the maxrss value as bytes rather than
            # kilobytes as on Linux.
            #
            # https://stackoverflow.com/questions/59913657/strange-values-of-get-rusage-maxrss-on-macos-and-linux
            rss_scale = 1000
        else:
            rss_scale = 1

        maxrss = usage.ru_maxrss // rss_scale

        usage = {
            "User time": usage.ru_utime,
            "System time": usage.ru_stime,
            "File system inputs": usage.ru_inblock,
            "File system outputs": usage.ru_oublock,
            "Socket messages sent": usage.ru_msgsnd,
            "Socket messages Received": usage.ru_msgrcv,
            "Signals received": usage.ru_nsignals,
            "Swaps": usage.ru_nswap,
            "Peak memory use (kB)": maxrss,
        }
        logging.info(f"Peak memory use: {maxrss} kB", extra=usage)
    except Exception as exc:
        logging.warning(
            f"Exception while trying to log ERT process resource usage: {exc}"
        )


def main():
    import locale

    locale.setlocale(locale.LC_NUMERIC, "C")

    args = ert_parser(None, sys.argv[1:])

    log_dir = os.path.abspath(args.logdir)
    try:
        os.makedirs(log_dir, exist_ok=True)
    except PermissionError as err:
        sys.exit(err)

    os.environ["ERT_LOG_DIR"] = log_dir

    with open(LOGGING_CONFIG, encoding="utf-8") as conf_file:
        logging.config.dictConfig(yaml.safe_load(conf_file))
    set_abort_handler(_log_util_abort)

    logger = logging.getLogger(__name__)
    if args.verbose:
        root_logger = logging.getLogger()
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        root_logger.addHandler(handler)

    FeatureToggling.update_from_args(args)
    try:
        with start_ert_server(args.mode), ErtPluginContext() as context:
            context.plugin_manager.add_logging_handle_to_root(logging.getLogger())
            logger.info(f"Running ert with {args}")
            log_config(args.config, logger)

            if FeatureToggling.is_enabled("experiment-server"):
                if args.mode != ENSEMBLE_EXPERIMENT_MODE:
                    raise NotImplementedError(
                        f"experiment-server can only run '{ENSEMBLE_EXPERIMENT_MODE}'"
                    )

            args.func(args)
    except ErtCliError as err:
        logger.exception(str(err))
        sys.exit(str(err))
    except BaseException as err:
        logger.exception(f'ERT crashed unexpectedly with "{err}"')

        logfiles = set()  # Use set to avoid duplicates...
        for handler in logging.getLogger().handlers:
            if isinstance(handler, logging.FileHandler):
                logfiles.add(handler.baseFilename)

        msg = f'ERT crashed unexpectedly with "{err}".\nSee logfile(s) for details:'
        msg += "\n   " + "\n   ".join(logfiles)

        sys.exit(msg)
    finally:
        os.environ.pop("ERT_LOG_DIR")


if __name__ == "__main__":
    main()
