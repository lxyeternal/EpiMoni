# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 16:03
# @Author  : blue
# @FileName: WorldCountriesModel.py
# @Software: PyCharm

from peewee import CharField, IntegerField,DateTimeField,TextField
from common.base.BaseModel import BaseModel


class WorldCountriesModel(BaseModel):
    class Meta:
        # 表名
        table_name = 'countries'
    id = IntegerField(primary_key=True)
    lastUpdateTime = DateTimeField() #  更新时间
    data = TextField() #  各国数据，是一个list