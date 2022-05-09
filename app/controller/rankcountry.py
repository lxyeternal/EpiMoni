# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 22:31
# @Author  : honywen
# @FileName: rankcountry.py
# @Software: PyCharm


import ast
from common.model.WorldCountriesModel import WorldCountriesModel


#  对两个list进行排序

def sortlist(namelist,valuelist):
    zip_dict = dict(zip(namelist, valuelist))
    sorted_dict = sorted(zip_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_name_list = list()
    sorted_value_list = list()
    for dict_ in sorted_dict:
        sorted_name_list.append(dict_[0])
        sorted_value_list.append(dict_[1])
    nametop10 = sorted_name_list[:10]
    valuetop10 = sorted_value_list[:10]
    nametop10.reverse()
    valuetop10.reverse()
    return [nametop10, valuetop10]


#  获取全球疫情热力图数据

def getrankdata():

    # date_string = datetime.now().strftime('%Y_%m_%d')
    worldmodel = WorldCountriesModel
    worldmodel = worldmodel.select().order_by(worldmodel.lastUpdateTime.desc()).limit(1)
    worlddata = ast.literal_eval(worldmodel[0].data)
    world_name_list = list()
    world_confirm_list = list()
    world_storeconfirm_list = list()
    world_dead_list = list()
    world_heal_list = list()
    for key in worlddata:
        world_name_list.append(key)
        confirm_value = worlddata[key][6]
        heal_value = worlddata[key][8]
        dead_value = worlddata[key][9]
        world_dead_list.append(dead_value)
        world_heal_list.append(heal_value)
        world_storeconfirm_list.append(confirm_value-heal_value-dead_value)
        world_confirm_list.append(confirm_value)
    storeconfirm_top10 = sortlist(world_name_list,world_storeconfirm_list)
    confirm_top10 = sortlist(world_name_list,world_confirm_list)
    dead_top10 = sortlist(world_name_list,world_dead_list)
    heal_top10 = sortlist(world_name_list,world_heal_list)

    return storeconfirm_top10,confirm_top10,dead_top10,heal_top10
