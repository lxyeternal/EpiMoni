# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 10:15
# @Author  : honywen
# @FileName: dbmaincountries.py
# @Software: PyCharm



from common.model.MainCountriesModel import MainCountries

def addmaincountries(tablename, lastUpdateTime, confirmedCount, confirmedIncr, curedCount, curedIncr, currentConfirmedCount, currentConfirmedIncr, deadCount, deadIncr, highDangerCount, midDangerCount, suspectedCount, suspectedCountIncr):

        maincountriesmodel = MainCountries(1,tablename)
        maincountriesmodel.lastUpdateTime = lastUpdateTime
        maincountriesmodel.confirmedCount = confirmedCount
        maincountriesmodel.confirmedIncr = confirmedIncr
        maincountriesmodel.curedCount = curedCount
        maincountriesmodel.curedIncr = curedIncr
        maincountriesmodel.currentConfirmedCount = currentConfirmedCount
        maincountriesmodel.currentConfirmedIncr = currentConfirmedIncr
        maincountriesmodel.deadCount = deadCount
        maincountriesmodel.deadIncr = deadIncr
        maincountriesmodel.highDangerCount = highDangerCount
        maincountriesmodel.midDangerCount = midDangerCount
        maincountriesmodel.suspectedCount = suspectedCount
        maincountriesmodel.suspectedCountIncr = suspectedCountIncr
        maincountriesmodel.save()