# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 11:22
# @Author  : honywen
# @FileName: maincountries.py
# @Software: PyCharm


from common.model.MainCountriesModel import MainCountries


#  获取重点国家疫情趋势数据
def gettrenddata():

    flag = 1
    trend_storeconfirm = list()
    trend_confirm = list()
    trend_heal = list()
    trend_dead = list()
    date_list = list()
    countries_name = ['us', 'brazil', 'france', 'germany', 'uk', 'russia', 'italy', 'spain']
    for name in countries_name:
        tablename = 'maincountries_' + name
        maincountriesmodel = MainCountries(0,tablename)
        maincountriesmodel = maincountriesmodel.select().order_by(maincountriesmodel.lastUpdateTime.desc()).limit(300)
        country_storeconfirm = list()
        country_confirm = list()
        country_heal = list()
        country_dead = list()
        for one in maincountriesmodel:
            if flag:
                date_time = one.lastUpdateTime
                date_string = date_time.strftime('%y-%m-%d')
                date_list.append(date_string)
            currentConfirmedCount = int(one.currentConfirmedCount)
            if currentConfirmedCount < 0:
                currentConfirmedCount = 0
            country_storeconfirm.append(currentConfirmedCount)
            country_confirm.append(int(one.confirmedCount))
            country_heal.append(int(one.curedCount))
            country_dead.append(int(one.deadCount))
        flag = 0
        country_storeconfirm.reverse()
        country_confirm.reverse()
        country_heal.reverse()
        country_dead.reverse()
        trend_storeconfirm.append(country_storeconfirm)
        trend_confirm.append(country_confirm)
        trend_heal.append(country_heal)
        trend_dead.append(country_dead)
    date_list.reverse()
    return date_list,trend_storeconfirm,trend_confirm,trend_heal,trend_dead


gettrenddata()