# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 16:04
# @Author  : blue
# @FileName: provinces.py
# @Software: PyCharm


from datetime import datetime
from common.model.ProvinceModel import ProvinceModel


def addprovinces(lastUpdateTime,data):

    lastUpdateTime = datetime.strptime(lastUpdateTime, '%Y-%m-%d %H:%M:%S')
    date_string = lastUpdateTime.strftime('%Y_%m_%d')
    provincesmodel = ProvinceModel()
    provincesmodel.lastUpdateTime = lastUpdateTime
    provincesmodel.data = data
    provincesmodel.save()