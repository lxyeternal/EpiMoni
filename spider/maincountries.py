# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 09:59
# @Author  : honywen
# @FileName: maincountries.py
# @Software: PyCharm

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DB.dbmaincountries import addmaincountries


#   采集重点国家的历史数据

def spider_maincountries():

    api_list = ['https://file1.dxycdn.com/2020/0315/553/3402160512808052518-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/559/3402160538577857305-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/929/3402160538577857318-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/631/3402160538577680475-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/364/3402160538577680395-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/629/3402160517102843039-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/993/3402160517102843054-135.json?t=27530034','https://file1.dxycdn.com/2020/0315/812/3402160512807875660-135.json?t=27530034']
    #  yidali :https://file1.dxycdn.com/2020/0315/993/3402160517102843054-135.json?t=27530034
    #  xibanya: https://file1.dxycdn.com/2020/0315/812/3402160512807875660-135.json?t=27530034
    #  yingguo: https://file1.dxycdn.com/2020/0315/364/3402160538577680395-135.json?t=27530034
    #  deguo: https://file1.dxycdn.com/2020/0315/631/3402160538577680475-135.json?t=27530034
    #  eluosi: https://file1.dxycdn.com/2020/0315/629/3402160517102843039-135.json?t=27530034
    #  baxi: https://file1.dxycdn.com/2020/0315/559/3402160538577857305-135.json?t=27530034
    #  faguo: https://file1.dxycdn.com/2020/0315/929/3402160538577857318-135.json?t=27530034
    countries_name = ['us','brazil','france','germany','uk','russia','italy','spain']
    for name in countries_name:
        filename = '../data/maincountry/area_trend_chart_' + name + '.json'
        tablename = 'maincountries_' + name
        fr = open(filename,'r')
        raw_json_data = json.loads(fr.read())['data']
        for one in raw_json_data:
            confirmedCount = one['confirmedCount']
            confirmedIncr = one['confirmedIncr']
            curedCount = one['curedCount']
            curedIncr = one['curedIncr']
            currentConfirmedCount = one['currentConfirmedCount']
            currentConfirmedIncr = one['currentConfirmedIncr']
            deadCount = one['deadCount']
            deadIncr = one['deadIncr']
            highDangerCount = one['highDangerCount']
            midDangerCount = one['midDangerCount']
            suspectedCount = one['suspectedCount']
            suspectedCountIncr = one['suspectedCountIncr']
            lastUpdateTime = one['dateId']

            # 每一条直接写入数据库中
            addmaincountries(tablename, lastUpdateTime, confirmedCount, confirmedIncr, curedCount, curedIncr,
                              currentConfirmedCount, currentConfirmedIncr, deadCount, deadIncr, highDangerCount,
                              midDangerCount, suspectedCount, suspectedCountIncr)


#   采集重点国家当日数据
def today_maincountries():
    countries_name_zn = ['美国','巴西','法国','德国','英国','俄罗斯','意大利','西班牙']
    countries_name = ['us','brazil','france','germany','uk','russia','italy','spain']
    url_api = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=330344037731'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    browser.get(url_api)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']
    areatree_json = raw_json_data['areaTree']
    for country in areatree_json:
        if country['name'] in countries_name_zn:
            name_index = countries_name_zn.index(country['name'])
            name = countries_name[name_index]
            lastUpdateTime = country['lastUpdateTime']
            tablename = 'maincountries_' + name
            country_today_confirm = country['today']['confirm']
            country_today_suspect = 0
            country_today_heal = country['today']['heal']
            country_today_dead = country['today']['dead']
            country_today_severe = 0
            #  total
            country_total_confirm = country['total']['confirm']
            country_total_suspect = country['total']['suspect']
            country_total_heal = country['total']['heal']
            country_total_dead = country['total']['dead']
            country_total_severe = country['total']['severe']
            country_today_storeConfirm = country_total_confirm-country_total_heal-country_total_dead

            # 写入数据库中
            addmaincountries(tablename, lastUpdateTime, country_total_confirm, country_today_confirm, country_total_heal, country_today_heal,
                             country_today_storeConfirm, country_today_confirm, country_total_dead, country_today_dead, country_today_severe,
                             country_total_severe, country_total_suspect, country_today_suspect)