# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 17:14
# @Author  : honywen
# @FileName: sh_news.py
# @Software: PyCharm



import json
from selenium import webdriver
from DB.shnews import addshanghainews
from selenium.webdriver.chrome.options import Options


#   采集上海每日的最新消息

def sh_news():
    sh_news_spi = 'https://api.dreamreader.qq.com/news/v1/province/news/list?province_code=sh&page_size=10'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path,chrome_options=chrome_options)
    browser.get(sh_news_spi)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']
    item_new = raw_json_data['items']
    for item in item_new:
        news_title = item['title']
        news_srcfrom = item['srcfrom']
        news_publish_time = item['publish_time']
        news_news_url = item['news_url']
        news_shortcut = item['shortcut']

        #  将数据写入到数据库中
        addshanghainews(news_publish_time,news_title,news_srcfrom,news_news_url,news_shortcut)

