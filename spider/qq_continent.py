# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 19:16
# @Author  : honywen
# @FileName: qq_continent.py
# @Software: PyCharm


#   爬取各大洲的数据，每日一采
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DB.continents import addcontinents


def qq_views():
    url_api = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path,chrome_options=chrome_options)
    browser.get(url_api)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']
    # 大洲各国数据采集
    womaboard_data = raw_json_data['WomAboard']
    '''
        每一个list保存一个大洲的数据
        依次分别是：亚洲，欧洲，非洲，大洋洲，北美洲，南美洲
        每一个list中保存的数据依次是：新增确诊，累计治愈，累计死亡，累计确诊
    '''
    contient_list = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    pub_date = womaboard_data[0]['pub_date']
    for country_data in womaboard_data:
        if country_data['continent'] == '亚洲':
            contient_list[0][0] = contient_list[0][0] + country_data['confirmAdd']
            contient_list[0][1] = contient_list[0][1] + country_data['heal']
            contient_list[0][2] = contient_list[0][2] + country_data['dead']
            contient_list[0][3] = contient_list[0][3] + country_data['confirm']
        elif country_data['continent'] == '欧洲':
            contient_list[1][0] = contient_list[1][0] + country_data['confirmAdd']
            contient_list[1][1] = contient_list[1][1] + country_data['heal']
            contient_list[1][2] = contient_list[1][2] + country_data['dead']
            contient_list[1][3] = contient_list[1][3] + country_data['confirm']
        elif country_data['continent'] == '非洲':
            contient_list[2][0] = contient_list[2][0] + country_data['confirmAdd']
            contient_list[2][1] = contient_list[2][1] + country_data['heal']
            contient_list[2][2] = contient_list[2][2] + country_data['dead']
            contient_list[2][3] = contient_list[2][3] + country_data['confirm']
        elif country_data['continent'] == '大洋洲':
            contient_list[3][0] = contient_list[3][0] + country_data['confirmAdd']
            contient_list[3][1] = contient_list[3][1] + country_data['heal']
            contient_list[3][2] = contient_list[3][2] + country_data['dead']
            contient_list[3][3] = contient_list[3][3] + country_data['confirm']
        elif country_data['continent'] == '北美洲':
            contient_list[4][0] = contient_list[4][0] + country_data['confirmAdd']
            contient_list[4][1] = contient_list[4][1] + country_data['heal']
            contient_list[4][2] = contient_list[4][2] + country_data['dead']
            contient_list[4][3] = contient_list[4][3] + country_data['confirm']
        elif country_data['continent'] == '南美洲':
            contient_list[5][0] = contient_list[5][0] + country_data['confirmAdd']
            contient_list[5][1] = contient_list[5][1] + country_data['heal']
            contient_list[5][2] = contient_list[5][2] + country_data['dead']
            contient_list[5][3] = contient_list[5][3] + country_data['confirm']
        else:
            pass

    #  写入数据库中
    addcontinents(pub_date,contient_list[0][0], contient_list[0][1], contient_list[0][2], contient_list[0][3],
                  contient_list[1][0], contient_list[1][1], contient_list[1][2], contient_list[1][3],
                  contient_list[2][0], contient_list[2][1], contient_list[2][2], contient_list[2][3],
                  contient_list[3][0], contient_list[3][1], contient_list[3][2], contient_list[3][3],
                  contient_list[4][0], contient_list[4][1], contient_list[4][2], contient_list[4][3],
                  contient_list[5][0], contient_list[5][1], contient_list[5][2], contient_list[5][3])

