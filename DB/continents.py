# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 19:17
# @Author  : honywen
# @FileName: continents.py
# @Software: PyCharm


from common.model.ContinentsModel import ContinentsModel

def addcontinents(lastUpdateTime, asia_addconfirm, asia_heal, asia_dead, asia_confirm, europe_addconfirm,
                      europe_heal, europe_dead, europe_confirm, africa_addconfirm, africa_heal, africa_dead,
                      africa_confirm, oceania_addconfirm, oceania_heal, oceania_dead, oceania_confirm,
                      northamerica_addconfirm, northamerica_heal, northamerica_dead, northamerica_confirm,
                      southamerica_addconfirm, southamerica_heal, southamerica_dead, southamerica_confirm):

        continentsmodel = ContinentsModel()
        continentsmodel.lastUpdateTime = lastUpdateTime
        continentsmodel.asia_addconfirm = asia_addconfirm
        continentsmodel.asia_heal = asia_heal
        continentsmodel.asia_dead = asia_dead
        continentsmodel.asia_confirm = asia_confirm
        continentsmodel.europe_addconfirm = europe_addconfirm
        continentsmodel.europe_heal = europe_heal
        continentsmodel.europe_dead = europe_dead
        continentsmodel.europe_confirm = europe_confirm
        continentsmodel.africa_addconfirm = africa_addconfirm
        continentsmodel.africa_heal = africa_heal
        continentsmodel.africa_dead = africa_dead
        continentsmodel.africa_confirm = africa_confirm
        continentsmodel.oceania_addconfirm = oceania_addconfirm
        continentsmodel.oceania_heal = oceania_heal
        continentsmodel.oceania_dead = oceania_dead
        continentsmodel.oceania_confirm = oceania_confirm
        continentsmodel.northamerica_addconfirm = northamerica_addconfirm
        continentsmodel.northamerica_heal = northamerica_heal
        continentsmodel.northamerica_dead = northamerica_dead
        continentsmodel.northamerica_confirm = northamerica_confirm
        continentsmodel.southamerica_addconfirm = southamerica_addconfirm
        continentsmodel.southamerica_heal = southamerica_heal
        continentsmodel.southamerica_dead = southamerica_dead
        continentsmodel.southamerica_confirm = southamerica_confirm

        continentsmodel.save()


#   查询数据库
def querycontinents():

        continentsmodel = ContinentsModel.select().order_by(ContinentsModel.lastUpdateTime.desc()).limit(1)
        continents_dead_list = list()
        continents_heal_list = list()
        continents_confirm_list = list()
        continents_addconfirm_list = list()
        continents_dead_value_list = [continentsmodel[0].asia_dead, continentsmodel[0].europe_dead,
                                      continentsmodel[0].africa_dead, continentsmodel[0].oceania_dead,
                                      continentsmodel[0].northamerica_dead, continentsmodel[0].southamerica_dead]
        continents_heal_value_list = [continentsmodel[0].asia_heal, continentsmodel[0].europe_heal,
                                      continentsmodel[0].africa_heal, continentsmodel[0].oceania_heal,
                                      continentsmodel[0].northamerica_heal, continentsmodel[0].southamerica_heal]
        continents_confirm_value_list = [continentsmodel[0].asia_confirm, continentsmodel[0].europe_confirm,
                                         continentsmodel[0].africa_confirm, continentsmodel[0].oceania_confirm,
                                         continentsmodel[0].northamerica_confirm,
                                         continentsmodel[0].southamerica_confirm]
        continents_addconfirm_value_list = [continentsmodel[0].asia_addconfirm, continentsmodel[0].europe_addconfirm,
                                            continentsmodel[0].africa_addconfirm, continentsmodel[0].oceania_addconfirm,
                                            continentsmodel[0].northamerica_addconfirm,
                                            continentsmodel[0].southamerica_addconfirm]
        contients_name = ['亚洲', '欧洲', '非洲', '大洋洲', '北美洲', '南美洲']
        for continent_value, continents_list, in zip(
                [continents_dead_value_list, continents_heal_value_list, continents_confirm_value_list,
                 continents_addconfirm_value_list],
                [continents_dead_list, continents_heal_list, continents_confirm_list, continents_addconfirm_list]):
                for index in range(len(contients_name)):
                        tmp_dict = dict()
                        tmp_dict['name'] = contients_name[index]
                        tmp_dict['value'] = int(continent_value[index])
                        continents_list.append(tmp_dict)
                # print(continents_list)
        return continents_dead_list, continents_heal_list, continents_confirm_list, continents_addconfirm_list
