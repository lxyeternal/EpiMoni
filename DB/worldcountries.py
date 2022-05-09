# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 16:05
# @Author  : blue
# @FileName: worldcountries.py
# @Software: PyCharm


from datetime import datetime
from common.model.WorldCountriesModel import WorldCountriesModel

def addcountries(lastUpdateTime,data):

    lastUpdateTime = datetime.strptime(lastUpdateTime, '%Y-%m-%d %H:%M:%S')
    date_string = lastUpdateTime.strftime('%Y_%m_%d')
    countriessmodel = WorldCountriesModel()
    countriessmodel.lastUpdateTime = lastUpdateTime
    countriessmodel.data = data
    countriessmodel.save()