# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 15:45
# @Author  : blue
# @FileName: ChinaDayModel.py.py
# @Software: PyCharm

from peewee import CharField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


# 國内數據統計
class ChinaDayModel(BaseModel):

    class Meta:
        table_name='chinaday'

    id = IntegerField(primary_key=True, unique=True)
    date = DateTimeField()
    extData = CharField()
    lastUpdateTime = DateTimeField()  #  数据更新时间
    oneday_today_confirm = CharField()  # 今日新增确诊
    oneday_today_suspect = CharField()  # 今日新增疑似
    oneday_today_heal = CharField()  # 今日新增治愈
    oneday_today_dead = CharField()  # 今日新增死亡
    oneday_today_storeConfirm = CharField()  # 现存确诊
    oneday_today_severe = CharField()  # 今日新增重症
    oneday_today_input = CharField()  # 今日新增境外输入
    oneday_total_confirm = CharField()  # 累计确诊
    oneday_total_suspect = CharField()  # 累计疑似
    oneday_total_heal = CharField()  # 累计治愈
    oneday_total_dead = CharField()  # 累计死亡
    oneday_total_severe = CharField()  # 累计重症
    oneday_total_input = CharField()  # 累计境外输入
