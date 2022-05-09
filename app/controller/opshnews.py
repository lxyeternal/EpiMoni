# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 17:29
# @Author  : honywen
# @FileName: opshnews.py
# @Software: PyCharm


from common.model.NewsModel import NewsModel


def get_shnews():
    sh_news_list = list()
    shanghainewsmodel = NewsModel
    shanghainewsmodel = shanghainewsmodel.select().order_by(shanghainewsmodel.news_publish_time.desc()).limit(8)
    for item in shanghainewsmodel:
        date_time = item.news_publish_time.strftime('%y-%m-%d %H:%M:%S')
        sh_news_list.append([item.news_title,date_time,item.news_srcfrom,item.news_news_url,item.news_shortcut])
    return sh_news_list