# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 12:35
# @Author  : honywen
# @FileName: shanghai.py
# @Software: PyCharm

import ast
from common.model.ShangHaiModel import ShangHaiModel
from common.model.ShangHaiAeraModel import ShangHaiAeraModel

def get_totaldata():
    shanghaimodel = ShangHaiModel
    shanghaimodel = shanghaimodel.select().order_by(shanghaimodel.lastUpdateTime.desc()).limit(1)
    today_total_confirm = shanghaimodel[0].sh_confirm
    today_new_confirmadd = shanghaimodel[0].sh_confirm_add
    today_total_dead = shanghaimodel[0].sh_dead
    today_total_heal = shanghaimodel[0].sh_heal
    today_new_dead = shanghaimodel[0].sh_newDead
    today_new_heal = shanghaimodel[0].sh_newHeal
    today_total_storeconfirm = int(today_total_confirm) - int(today_total_dead) - int(today_total_heal)
    today_new_storeconfirm = int(today_new_confirmadd) - int(today_new_dead) - int(today_new_heal)
    return today_total_storeconfirm,today_total_confirm,today_total_dead,today_total_heal,today_new_storeconfirm,today_new_confirmadd,today_new_dead,today_new_heal

def get_shzhexain():
    zhexain_data = [[],[],[],[],[],[]]
    date_list = list()
    shanghaimodel = ShangHaiModel
    shanghaimodel = shanghaimodel.select().order_by(shanghaimodel.lastUpdateTime.desc()).limit(30)
    for ondedate in shanghaimodel:
        date_time = ondedate.lastUpdateTime
        date_string = date_time.strftime('%y-%m-%d')
        date_list.append(date_string)
        zhexain_data[0].append(int(ondedate.sh_confirm))
        zhexain_data[1].append(int(ondedate.sh_confirm_add))
        zhexain_data[2].append(int(ondedate.sh_dead))
        zhexain_data[3].append(int(ondedate.sh_heal))
        zhexain_data[4].append(int(ondedate.sh_newDead))
        zhexain_data[5].append(int(ondedate.sh_newHeal))
    for list_ in zhexain_data:
        list_.reverse()
    date_list.reverse()
    return date_list,zhexain_data

def get_peidata():
    sh_pei_list = list()
    shaeramodel = ShangHaiAeraModel
    shaeramodel = shaeramodel.select().order_by(shaeramodel.lastUpdateTime.desc()).limit(1)
    shaeradata = ast.literal_eval(shaeramodel[0].data)
    for key in shaeradata:
        if key in ['地区待确认']:
            pass
        else:
            tmp = dict()
            tmp['name'] = key
            tmp['value'] = shaeradata[key][2]
            sh_pei_list.append(tmp)
    return sh_pei_list

def shrate():
    shhealrate_list = list()
    shdeadrate_list = list()
    shdaymodel = ShangHaiModel
    shdaymodel = shdaymodel.select().order_by(shdaymodel.lastUpdateTime.desc()).limit(60)
    for oneday in shdaymodel:
        heal_rate = round(int(oneday.sh_heal) / int(oneday.sh_confirm) * 100, 2)
        dead_rate = round(int(oneday.sh_dead) / int(oneday.sh_confirm) * 100, 2)
        date_time = oneday.lastUpdateTime
        date_string = date_time.strftime('%y-%m-%d')
        shhealrate_list.append([date_string, heal_rate])
        shdeadrate_list.append([date_string, dead_rate])
    shhealrate_list.reverse()
    shdeadrate_list.reverse()
    return shhealrate_list, shdeadrate_list