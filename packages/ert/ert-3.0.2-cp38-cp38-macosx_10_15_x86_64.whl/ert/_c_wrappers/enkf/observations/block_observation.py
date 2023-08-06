#  Copyright (C) 2012  Equinor ASA, Norway.
#
#  The file 'block_obs.py' is part of ERT - Ensemble based Reservoir Tool.
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
from typing import Union

from cwrap import BaseCClass
from ecl.grid import EclGrid

from ert import _clib
from ert._c_wrappers import ResPrototype
from ert._c_wrappers.enkf.config import FieldConfig
from ert._c_wrappers.enkf.node_id import NodeId
from ert._c_wrappers.enkf.observations import BlockDataConfig


class BlockObservation(BaseCClass):
    TYPE_NAME = "block_obs"

    _alloc = ResPrototype(
        "void*  block_obs_alloc( char* , block_data_config , ecl_grid )", bind=False
    )
    _free = ResPrototype("void   block_obs_free( block_obs )")
    _iget_i = ResPrototype("int    block_obs_iget_i(block_obs, int)")
    _iget_j = ResPrototype("int    block_obs_iget_j( block_obs, int)")
    _iget_k = ResPrototype("int    block_obs_iget_k( block_obs , int)")
    _get_size = ResPrototype("int    block_obs_get_size( block_obs )")
    _get_std = ResPrototype("double block_obs_iget_std( block_obs, int )")
    _get_std_scaling = ResPrototype(
        "double block_obs_iget_std_scaling( block_obs, int )"
    )
    _get_value = ResPrototype("double block_obs_iget_value( block_obs, int)")
    _get_depth = ResPrototype("double block_obs_iget_depth( block_obs, int)")
    _add_field_point = ResPrototype(
        "void   block_obs_append_field_obs( block_obs, int,int,int,double,double)"
    )
    _add_summary_point = ResPrototype(
        "void   block_obs_append_summary_obs( block_obs, int, int, int, double, double)"
    )
    _iget_data = ResPrototype(
        "double block_obs_iget_data(block_obs, void*, int, node_id)"
    )

    def __init__(
        self, obs_key, data_config: Union[BlockDataConfig, FieldConfig], grid: EclGrid
    ):
        c_ptr = self._alloc(obs_key, data_config, grid)
        super().__init__(c_ptr)

    def getCoordinate(self, index):
        """@rtype: tuple of (int, int, int)"""
        i = self._iget_i(index)
        j = self._iget_j(index)
        k = self._iget_k(index)
        return i, j, k

    def __len__(self):
        """@rtype: int"""
        return self._get_size()

    def __iter__(self):
        cur = 0
        while cur < len(self):
            yield cur
            cur += 1

    def addPoint(self, i, j, k, value, std, sum_key=None):
        if sum_key is None:
            self._add_field_point(i, j, k, value, std)
        else:
            self._add_summary_point(i, j, k, sum_key, value, std)

    def getValue(self, index):
        """@rtype: float"""
        return self._get_value(index)

    def getStd(self, index):
        """@rtype: float"""
        return self._get_std(index)

    def getStdScaling(self, index):
        """@rtype: float"""
        return self._get_std_scaling(index)

    def updateStdScaling(self, factor, active_list):
        _clib.local.block_obs.update_std_scaling(self, factor, active_list)

    def getDepth(self, index):
        """@rtype: float"""
        return self._get_depth(index)

    def getData(self, state, obs_index, node_id: NodeId):
        """
        @type state: c_void_p
        @type obs_index: int
        @type node_id: NodeId
        @rtype: float"""

        return self._iget_data(state, obs_index, node_id)

    def free(self):
        self._free()

    def __repr__(self):
        return f"BlockObservation(size = {len(self)}) at 0x{self._address():x}"
