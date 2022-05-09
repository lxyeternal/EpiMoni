# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 22:31
# @Author  : honywen
# @FileName: worldmap.py
# @Software: PyCharm

import ast
import numpy as np
from common.model.WorldCountriesModel import WorldCountriesModel

#  获取全球疫情热力图数据

def getworldmap():

    worldmap_data = list()
    worldmodel = WorldCountriesModel
    worldmodel = worldmodel.select().order_by(worldmodel.lastUpdateTime.desc()).limit(1)
    worlddata = ast.literal_eval(worldmodel[0].data)
    world_name_list = list()
    world_confirm_list = list()
    world_storeconfirm_list = list()
    for key in worlddata:
        world_name_list.append(key)
        confirm_value = worlddata[key][6]
        heal_value = worlddata[key][8]
        dead_value = worlddata[key][9]
        world_storeconfirm_list.append(confirm_value-heal_value-dead_value)
        world_confirm_list.append(confirm_value)
    for name, value in zip(world_name_list,world_storeconfirm_list):
        tmp = dict()
        tmp['name'] = name
        tmp['value'] = value
        worldmap_data.append(tmp)
    maxvalue = np.median(world_storeconfirm_list)
    world_name_list.reverse()
    world_confirm_list.reverse()
    world_storeconfirm_list.reverse()
    return worldmap_data,world_name_list,world_confirm_list,world_storeconfirm_list
