# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 15:58
# @Author  : blue
# @FileName: ProvinceModel.py.py
# @Software: PyCharm



from peewee import IntegerField,DateTimeField,TextField
from common.base.BaseModel import BaseModel



class ProvinceModel(BaseModel):
    class Meta:
        # 表名
        table_name = 'province'
    id = IntegerField(primary_key=True)
    lastUpdateTime = DateTimeField()  #  更新时间
    data = TextField()  #  各省数据，是一个list
