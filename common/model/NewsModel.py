# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 17:18
# @Author  : honywen
# @FileName: NewsModel.py
# @Software: PyCharm



from peewee import CharField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


# 实时新闻
class NewsModel(BaseModel):

    class Meta:
        table_name = 'shanghainews'

    id = IntegerField(primary_key=True, unique=True)
    news_publish_time = DateTimeField()  #  更新时间
    news_title = CharField()#  新闻标题
    news_srcfrom = CharField()#  新闻来源
    news_news_url = CharField()#  新闻链接
    news_shortcut = CharField()#  截图链接