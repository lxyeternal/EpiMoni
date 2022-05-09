# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 14:43
# @Author  : blue
# @FileName: UserModel.py
# @Software: PyCharm


from peewee import CharField, BooleanField, IntegerField,DateTimeField
from common.base.BaseModel import BaseModel


# 管理员工号
class UserModel(BaseModel):

    class Meta:
        table_name='user'

    id = IntegerField(primary_key=True,unique=True)
    username = CharField()  # 用户名
    password = CharField()  # 密码
    fullname = CharField()  # 真实性名
    email = CharField()  # 邮箱
    phone = CharField()  # 电话
    status = BooleanField(default=True)  # 生效失效标识