# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 21:40
# @Author  : honywen
# @FileName: nationmap.py
# @Software: PyCharm

import ast
import numpy as np
from common.model.ProvinceModel import ProvinceModel


#  获取全国疫情热力图数据
def getnationmap():

    nationmap_data = list()
    provincesmodel = ProvinceModel
    provincesmodel = provincesmodel.select().order_by(provincesmodel.lastUpdateTime.desc()).limit(1)
    provincesdata = ast.literal_eval(provincesmodel[0].data)
    provinces_name_list = list()
    provinces_confirm_list = list()
    provinces_storeconfirm_list = list()
    for key in provincesdata:
        provinces_name_list.append(key)
        confirm_value = provincesdata[key][6]
        heal_value = provincesdata[key][8]
        dead_value = provincesdata[key][9]
        provinces_storeconfirm_list.append(confirm_value-heal_value-dead_value)
        provinces_confirm_list.append(confirm_value)
    for name, value in zip(provinces_name_list,provinces_storeconfirm_list):
        tmp = dict()
        tmp['name'] = name
        tmp['value'] = value
        nationmap_data.append(tmp)
    maxvalue = np.median(provinces_storeconfirm_list)
    provinces_name_list.reverse()
    provinces_confirm_list.reverse()
    provinces_storeconfirm_list.reverse()
    return nationmap_data,provinces_name_list,provinces_confirm_list,provinces_storeconfirm_list,maxvalue

