# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 09:41
# @Author  : honywen
# @FileName: shaera.py
# @Software: PyCharm


from common.model.ShangHaiAeraModel import ShangHaiAeraModel

def addshaera(lastUpdateTime, data):

    shaeramodel = ShangHaiAeraModel()
    shaeramodel.lastUpdateTime = lastUpdateTime
    shaeramodel.data = data

    shaeramodel.save()