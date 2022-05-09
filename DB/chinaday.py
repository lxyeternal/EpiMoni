# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 16:04
# @Author  : blue
# @FileName: chinaday.py
# @Software: PyCharm


from common.model.ChinaDayModel import ChinaDayModel

def addchinaday(date,extData,lastUpdateTime,oneday_today_confirm,oneday_today_suspect,oneday_today_heal,oneday_today_dead,oneday_today_storeConfirm,oneday_today_severe,oneday_today_input,oneday_total_confirm,oneday_total_suspect,oneday_total_heal,oneday_total_dead,oneday_total_severe,oneday_total_input):

    chinadaymodel = ChinaDayModel()
    chinadaymodel.date = date
    chinadaymodel.extData = extData
    chinadaymodel.lastUpdateTime = lastUpdateTime
    chinadaymodel.oneday_today_confirm = oneday_today_confirm
    chinadaymodel.oneday_today_suspect = oneday_today_suspect
    chinadaymodel.oneday_today_heal = oneday_today_heal
    chinadaymodel.oneday_today_dead = oneday_today_dead
    chinadaymodel.oneday_today_storeConfirm = oneday_today_storeConfirm
    chinadaymodel.oneday_today_severe = oneday_today_severe
    chinadaymodel.oneday_today_input = oneday_today_input
    chinadaymodel.oneday_total_confirm = oneday_total_confirm
    chinadaymodel.oneday_total_suspect = oneday_total_suspect
    chinadaymodel.oneday_total_heal = oneday_total_heal
    chinadaymodel.oneday_total_dead = oneday_total_dead
    chinadaymodel.oneday_total_severe = oneday_total_severe
    chinadaymodel.oneday_total_input = oneday_total_input
    chinadaymodel.save()