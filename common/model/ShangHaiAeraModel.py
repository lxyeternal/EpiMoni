# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 00:16
# @Author  : honywen
# @FileName: ShangHaiAeraModel.py
# @Software: PyCharm

from peewee import TextField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


#   上海各区数据库模型
class ShangHaiAeraModel(BaseModel):

    class Meta:
        table_name = 'shanghaiaera'

    id = IntegerField(primary_key=True, unique=True)
    lastUpdateTime = DateTimeField()  # 更新时间
    data = TextField()  #   各区的数据，是一个list