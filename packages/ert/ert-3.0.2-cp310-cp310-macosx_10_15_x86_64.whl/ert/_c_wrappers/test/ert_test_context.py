#  Copyright (C) 2013  Equinor ASA, Norway.
#
#  This file is part of ERT - Ensemble based Reservoir Tool.
#
#  ERT is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ERT is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU General Public License at <http://www.gnu.org/licenses/gpl.html>
#  for more details.
import os.path
import pathlib
import shutil
import tempfile
from distutils.dir_util import copy_tree

from ert._c_wrappers.enkf import EnKFMain, ResConfig


class ErtTestContext:
    def __init__(self, model_config):
        self._tmp_dir = tempfile.mkdtemp()
        self._model_config = model_config
        self._res_config = None
        self._ert = None
        self._dir_before = None

    def __enter__(self):
        self._dir_before = os.getcwd()
        os.chdir(self._tmp_dir)
        try:
            directory = pathlib.Path(self._model_config).parent
            config = pathlib.Path(self._model_config).name
            copy_tree(directory, self._tmp_dir)
            self._res_config = ResConfig(user_config_file=config)
            self._ert = EnKFMain(self._res_config, strict=True)
        except Exception:
            os.chdir(self._dir_before)
            shutil.rmtree(self._tmp_dir, ignore_errors=True)
            raise
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._ert = None
        self._res_config = None
        os.chdir(self._dir_before)
        shutil.rmtree(self._tmp_dir, ignore_errors=True)

    def getErt(self):
        return self._ert

    def getCwd(self):
        return os.getcwd()

    def installWorkflowJob(self, job_name, job_path):
        """@rtype: bool"""
        if os.path.exists(job_path) and os.path.isfile(job_path):
            ert = self.getErt()
            # pylint: disable=no-member
            workflow_list = ert.getWorkflowList()

            workflow_list.addJob(job_name, job_path)
        else:
            raise IOError(f"Could not load workflowjob from:{job_path}")

    def runWorkflowJob(self, job_name, *arguments):
        """@rtype: bool"""
        ert = self.getErt()
        # pylint: disable=no-member
        workflow_list = ert.getWorkflowList()

        if workflow_list.hasJob(job_name):
            job = workflow_list.getJob(job_name)
            job.run(ert, arguments)
            return True
        return False


class ErtTestSharedContext:
    """
    Like ErtTestContext without making a private copy of the testcase.
    Primarily for benchmarking large tests which we don't want to copy.

    Use with caution and be careful with state in the testcase!
    """

    def __init__(self, model_config, cleanup=True):
        """
        If 'cleanup==True' exiting the context removes all files and
        directories which did not exist when entering the context.

        It will NOT, however, restore changed content of existing files.
        """
        self._model_config = model_config
        self._cleanup = cleanup
        self._res_config = None
        self._ert = None
        self._dir_before = None
        self._dir_list = {}
        self._file_list = {}

    def __enter__(self):
        self._dir_before = os.getcwd()
        os.chdir(pathlib.Path(self._model_config).parent)

        # store all files upon entering
        if self._cleanup:
            self._dir_list = {
                os.path.join(root, d)
                for root, dirs, files in os.walk(".")
                for d in dirs
            }
            self._file_list = {
                os.path.join(root, f)
                for root, dirs, files in os.walk(".")
                for f in files
            }
        try:
            config = pathlib.Path(self._model_config).name
            self._res_config = ResConfig(user_config_file=config)
            self._ert = EnKFMain(self._res_config, strict=True)
        except Exception:
            os.chdir(self._dir_before)
            raise
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._cleanup:
            # remove any files not present when entering
            fl = {
                os.path.join(root, f)
                for root, dirs, files in os.walk(".")
                for f in files
            }
            dl = {
                os.path.join(root, d)
                for root, dirs, files in os.walk(".")
                for d in dirs
            }
            for _file in fl - self._file_list:
                os.remove(_file)
            for _dir in dl - self._dir_list:
                shutil.rmtree(_dir, ignore_errors=True)

        self._ert = None
        self._res_config = None
        os.chdir(self._dir_before)

    @property
    def ert(self):
        return self._ert
