# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 17:22
# @Author  : honywen
# @FileName: shnews.py
# @Software: PyCharm


from common.model.NewsModel import NewsModel

def addshanghainews(news_publish_time,news_title,news_srcfrom,news_news_url,news_shortcut):

    shanghainewsmodel = NewsModel()
    shanghainewsmodel.news_publish_time = news_publish_time
    shanghainewsmodel.news_title = news_title
    shanghainewsmodel.news_srcfrom = news_srcfrom
    shanghainewsmodel.news_news_url = news_news_url
    shanghainewsmodel.news_shortcut = news_shortcut

    shanghainewsmodel.save()
