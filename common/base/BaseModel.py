# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 9:39
# @Author  : blue
# @FileName: BaseModel.py
# @Software: PyCharm

from peewee import MySQLDatabase, Model
from conf.config import config
import os

config = config[os.getenv('FLASK_CONFIG') or 'default']
db = MySQLDatabase(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWD, database=config.DB_DATABASE, charset=config.CHARSET)

class BaseModel(Model):
    class Meta:
        database = db