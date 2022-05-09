# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 14:53
# @Author  : honywen
# @FileName: indexdata.py
# @Software: PyCharm

import ast
from common.model.ProvinceModel import ProvinceModel
from common.model.ChinaDayModel import ChinaDayModel

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


def cntotaldata():

    chinadaymodel = ChinaDayModel
    chinadaymodel = chinadaymodel.select().order_by(chinadaymodel.date.desc()).limit(1)
    today_storeconfirm = int(chinadaymodel[0].oneday_total_confirm) - int(chinadaymodel[0].oneday_total_dead) - int(chinadaymodel[0].oneday_total_heal)
    today_data = [today_storeconfirm,chinadaymodel[0].oneday_total_confirm,chinadaymodel[0].oneday_total_heal,chinadaymodel[0].oneday_total_dead,chinadaymodel[0].oneday_today_confirm,chinadaymodel[0].oneday_today_confirm,chinadaymodel[0].oneday_today_heal,chinadaymodel[0].oneday_today_dead]
    return today_data


def cnzhexian():
    date_list = list()
    cnzhexain_data = [[], [], [], [], []]
    chinadaymodel = ChinaDayModel
    chinadaymodel = chinadaymodel.select().order_by(chinadaymodel.date.desc()).limit(60)
    for oneday in chinadaymodel:
        oneday_storeconfirm = int(oneday.oneday_total_confirm) - int(oneday.oneday_total_dead) - int(oneday.oneday_total_heal)
        date_time = oneday.date
        date_string = date_time.strftime('%y-%m-%d')
        date_list.append(date_string)
        cnzhexain_data[0].append(oneday_storeconfirm)
        cnzhexain_data[1].append(int(oneday.oneday_total_confirm))
        cnzhexain_data[2].append(int(oneday.oneday_total_heal))
        cnzhexain_data[3].append(int(oneday.oneday_total_dead))
        cnzhexain_data[4].append(int(oneday.oneday_today_confirm))
    for list_ in cnzhexain_data:
        list_.reverse()
    date_list.reverse()
    return date_list,cnzhexain_data

def cnpeidata():
    cnpie_list = list()
    provincesmodel = ProvinceModel
    provincesmodel = provincesmodel.select().order_by(provincesmodel.lastUpdateTime.desc()).limit(1)
    provincesdata = ast.literal_eval(provincesmodel[0].data)
    provinces_name_list = list()
    provinces_confirm_list = list()
    for key in provincesdata:
        provinces_name_list.append(key)
        confirm_value = provincesdata[key][6]
        provinces_confirm_list.append(confirm_value)
    sorteddata= sortlist(provinces_name_list,provinces_confirm_list)
    for name, value in zip(sorteddata[0], sorteddata[1]):
        tmp = dict()
        tmp['name'] = name
        tmp['value'] = value
        cnpie_list.append(tmp)
    return sorteddata[0],cnpie_list


def cnstorecf():
    storeconfirm_list = list()
    provincesmodel = ProvinceModel
    provincesmodel = provincesmodel.select().order_by(provincesmodel.lastUpdateTime.desc()).limit(1)
    provincesdata = ast.literal_eval(provincesmodel[0].data)
    mainland = 0
    for key in provincesdata:
        confirm_value = provincesdata[key][6]
        heal_value = provincesdata[key][8]
        dead_value = provincesdata[key][9]
        storeconfirm = confirm_value - heal_value - dead_value
        if key in ['香港','台湾','澳门']:
            tmp = dict()
            tmp['name'] = key
            tmp['value'] = storeconfirm
            storeconfirm_list.append(tmp)
        else:
            mainland = mainland + storeconfirm
    tmp_ = dict()
    tmp_['name'] = '31省市现有确诊'
    tmp_['value'] = mainland
    storeconfirm_list.append(tmp_)
    return storeconfirm_list

def cnhealrate():
    cnhealrate_list = list()
    cndeadrate_list = list()
    chinadaymodel = ChinaDayModel
    chinadaymodel = chinadaymodel.select().order_by(chinadaymodel.date.desc()).limit(60)
    for oneday in chinadaymodel:
        heal_rate = round(int(oneday.oneday_total_heal)/int(oneday.oneday_total_confirm) * 100, 2)
        dead_rate = round(int(oneday.oneday_total_dead)/int(oneday.oneday_total_confirm) * 100, 2)
        date_time = oneday.date
        date_string = date_time.strftime('%y-%m-%d')
        cnhealrate_list.append([date_string,heal_rate])
        cndeadrate_list.append([date_string,dead_rate])
    cnhealrate_list.reverse()
    cndeadrate_list.reverse()
    return cnhealrate_list, cndeadrate_list