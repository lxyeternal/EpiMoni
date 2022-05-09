# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/7 10:33
# @Author  : honywen
# @FileName: spidermain.py
# @Software: PyCharm

import time
from spider.qq_continent import qq_views
from spider.sh_news import sh_news
from spider.wangyi import worldinfo, chinatoday
from spider.maincountries import today_maincountries
from spider.wangyi_shanghai import today_shanghai, spider_shanghaiaera


def auto_main():
    #  上海市数据采集
    today_shanghai()
    spider_shanghaiaera()
    sh_news()
    #  各大洲每日数据采集
    qq_views()
    #  主要国家数据采集
    today_maincountries()
     # 中国各省市和世界各国数据采集
    worldinfo()
    # #  中国今日数据采集
    chinatoday()


if __name__ == '__main__':
    while True:
        time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
        if time_now == "01:30:00":  # 此处设置每天定时的时间
            auto_main()
            subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "自动数据采集完成"
            print(subject)
            time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次


