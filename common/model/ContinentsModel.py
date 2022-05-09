# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 19:04
# @Author  : honywen
# @FileName: ContinentsModel.py
# @Software: PyCharm


from peewee import CharField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


# 國内數據統計
class ContinentsModel(BaseModel):

    class Meta:
        table_name = 'continents'

    id = IntegerField(primary_key=True, unique=True)
    lastUpdateTime = DateTimeField()  #  数据更新时间
    asia_addconfirm = CharField()  # 亚洲新增确诊
    asia_heal = CharField()  #  亚洲累计治愈
    asia_dead = CharField()  # 亚洲累计死亡
    asia_confirm = CharField()  #  亚洲累计确诊
    europe_addconfirm = CharField()  # 欧洲
    europe_heal = CharField()
    europe_dead = CharField()
    europe_confirm = CharField()
    africa_addconfirm = CharField() # 非洲
    africa_heal = CharField()
    africa_dead = CharField()
    africa_confirm = CharField()
    oceania_addconfirm = CharField() # 大洋洲
    oceania_heal = CharField()
    oceania_dead = CharField()
    oceania_confirm = CharField()
    northamerica_addconfirm = CharField() # 北美洲
    northamerica_heal = CharField()
    northamerica_dead = CharField()
    northamerica_confirm = CharField()
    southamerica_addconfirm = CharField() # 南美洲
    southamerica_heal = CharField()
    southamerica_dead = CharField()
    southamerica_confirm = CharField()
