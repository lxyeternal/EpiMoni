# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 23:42
# @Author  : honywen
# @FileName: wangyi_shanghai.py
# @Software: PyCharm


import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DB.dbshanghai import addshanghai
from DB.shaera import addshaera


def spider_shanghai():      #   上海历史数据采集
    url_api = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=%E4%B8%8A%E6%B5%B7&limit=60&'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path,chrome_options=chrome_options)
    browser.get(url_api)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']
    for oneday in raw_json_data:
        day_confirm = str(oneday['confirm'])
        day_confirm_add = oneday['confirm_add']
        day_dead = str(oneday['dead'])
        day_heal = str(oneday['heal'])
        day_newConfirm = str(oneday['newConfirm'])
        day_newDead = str(oneday['newDead'])
        day_newHeal = str(oneday['newHeal'])
        day_wzz = str(oneday['wzz'])
        day_wzz_add = str(oneday['wzz_add'])
        day_lastupdatetime = str(oneday['year']) + '.' + oneday['date']

        #  将数据写入数据库中
        addshanghai(day_lastupdatetime, day_confirm, day_confirm_add, day_dead, day_heal, day_newConfirm, day_newDead, day_newHeal, day_wzz, day_wzz_add)


def today_shanghai():      #   上海当日数据采集
    url_api = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=%E4%B8%8A%E6%B5%B7&limit=60&'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path,chrome_options=chrome_options)
    browser.get(url_api)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']
    oneday = raw_json_data[-1:][0]
    day_confirm = str(oneday['confirm'])
    day_confirm_add = oneday['confirm_add']
    day_dead = str(oneday['dead'])
    day_heal = str(oneday['heal'])
    day_newConfirm = str(oneday['newConfirm'])
    day_newDead = str(oneday['newDead'])
    day_newHeal = str(oneday['newHeal'])
    day_wzz = str(oneday['wzz'])
    day_wzz_add = str(oneday['wzz_add'])
    day_lastupdatetime = str(oneday['year']) + '.' + oneday['date']

    #  将数据写入数据库中
    addshanghai(day_lastupdatetime, day_confirm, day_confirm_add, day_dead, day_heal, day_newConfirm, day_newDead, day_newHeal, day_wzz, day_wzz_add)




def spider_shanghaiaera():   #   当日数据采集
    shanghaiaera_api = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    browser.get(shanghaiaera_api)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']['diseaseh5Shelf']['areaTree'][0]['children']
    for onecity in raw_json_data:
        if onecity['name'] == '上海':
            shanghai_children = onecity['children']
            aeradata_dict = dict()
            date = ''
            for aera in shanghai_children:
                aera_name = aera['name']
                date = aera['date']
                aera_today_confirm = aera['today']['confirm']
                aera_today_confirmCuts = aera['today']['confirmCuts']

                aera_total_confirm = aera['total']['confirm']
                aera_total_highRiskAreaNum = aera['total']['highRiskAreaNum']
                aera_total_heal = aera['total']['heal']
                aera_total_dead = aera['total']['dead']
                aera_total_mediumRiskAreaNum = aera['total']['mediumRiskAreaNum']
                aera_total_nowConfirm = aera['total']['nowConfirm']

                aeradata_dict[aera_name] = [aera_today_confirm,aera_today_confirmCuts,aera_total_confirm,aera_total_highRiskAreaNum,aera_total_heal,aera_total_dead,aera_total_mediumRiskAreaNum,aera_total_nowConfirm]
            #  数据插入数据库
            addshaera(date,aeradata_dict)