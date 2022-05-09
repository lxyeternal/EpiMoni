# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 23:49
# @Author  : honywen
# @FileName: ShangHaiModel.py
# @Software: PyCharm


from peewee import CharField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


# 國内數據統計
class ShangHaiModel(BaseModel):

    class Meta:
        table_name = 'shanghaiday'

    id = IntegerField(primary_key=True, unique=True)
    lastUpdateTime = DateTimeField()   #  更新时间
    sh_confirm = CharField()   #  上海累计确诊
    sh_confirm_add = CharField()   #  上海新增确诊
    sh_dead = CharField()   #  上海累计死亡
    sh_heal = CharField()   #  上海累计治愈
    sh_newConfirm = CharField()   #  上海新增确诊
    sh_newDead = CharField()   #  上海新增死亡
    sh_newHeal = CharField()   #  上海新增治愈
    sh_wzz = CharField()   #  没用到
    sh_wzz_add = CharField()   #  没用到