# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 10:00
# @Author  : honywen
# @FileName: MainCountriesModel.py
# @Software: PyCharm

from peewee import CharField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


# 重点国家疫情数据数据库模型
def MainCountries(flag,tablename):

    class MainCountriesModel(BaseModel):
        class Meta:
            # 表名
            table_name = tablename
        id = IntegerField(primary_key=True)
        lastUpdateTime = DateTimeField(default=0)  #  更新时间
        confirmedCount = CharField()  #  累计确诊
        confirmedIncr = CharField(default=0)  #  新增确诊
        curedCount = CharField(default=0)  #  累计治愈
        curedIncr = CharField(default=0)  #  新增治愈
        currentConfirmedCount = CharField(default=0)  #  今日现存确诊累计
        currentConfirmedIncr = CharField(default=0)  #  今日新增现存确诊
        deadCount = CharField(default=0)  #  累计死亡
        deadIncr = CharField(default=0)  #  新增死亡
        highDangerCount = CharField(default=0)  #  累计高危
        midDangerCount = CharField(default=0)  #  累计中威
        suspectedCount = CharField(default=0)  #  累计意疑似
        suspectedCountIncr = CharField(default=0)  #  今日新增疑似
    if flag:
        return MainCountriesModel()
    else:
        return MainCountriesModel

