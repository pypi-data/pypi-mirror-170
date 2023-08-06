import sys

from ert.shared.services._base_service import BaseService


class WebvizErt(BaseService):
    service_name = "webviz-ert"

    def __init__(
        self, title: str = None, experimental_mode: bool = False, verbose: bool = False
    ):
        exec_args = [sys.executable, "-m", "webviz_ert"]
        if experimental_mode:
            exec_args.append("--experimental-mode")
        if verbose:
            exec_args.append("--verbose")
        if title:
            exec_args.append("--title")
            exec_args.append(title)
        super().__init__(exec_args)
