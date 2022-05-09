# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/6 18:52
# @Author  : honywen
# @FileName: predict.py
# @Software: PyCharm

import math
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from common.model.ChinaDayModel import ChinaDayModel
from common.model.MainCountriesModel import MainCountries
from common.model.ShangHaiModel import ShangHaiModel
from common.model.WorldCountriesModel import WorldCountriesModel



# def pridict_main(timelist,personlist,future,r,t0):
#     #  日期及感染人数
#     time_array = np.array(timelist)
#     confirm_array = np.array(personlist)
#
#     # 用最小二乘法估计拟合
#     # 现有数据曲线拟合检验
#     popt1, pcov1 = curve_fit(logistic_increase_function, time_array, confirm_array)
#
#     # 获取popt里面是拟合系数
#     print("K:capacity  P0:initial_value   r:increase_rate   t:time")
#     print(popt1)
#     # 拟合后预测的P值
#
#     confirm_array_predict = logistic_increase_function(time_array, popt1[0], popt1[1], r_, t0_)
#     # 未来预测
#     future = np.array(future)
#     future_predict = logistic_increase_function(future, popt1[0], popt1[1], r_, t0_)
#     future_predict_list = future_predict.tolist()
#     print(future_predict_list)
#     future_predict_list = [int(i) for i in future_predict_list]
#     print(future_predict_list)
#     # 绘图
#     plt.plot(time_array, confirm_array, 's', label="confimed people")
#     plt.plot(time_array, confirm_array_predict, 'r', label='predict people')
#     plt.plot(future, future_predict, 's', label='future predict people')
#     plt.xlabel('time')
#     plt.ylabel('confimed people')
#     plt.legend(loc=0)  # 指定legend的位置右下角
#
#     print(logistic_increase_function(np.array(28), popt1[0], popt1[1], r_, t0_))
#     print(logistic_increase_function(np.array(29), popt1[0], popt1[1], r_, t0_))
#     plt.show()
#     return future_predict_list


#   针对全国疫情发展预测
def predict_china():
    count = 0
    future = list()
    time_list = list()
    addconfirm_list = list()
    all_date = list()
    chinadaymodel = ChinaDayModel
    chinadaymodel = chinadaymodel.select().order_by(chinadaymodel.date.asc()).limit()
    for index in chinadaymodel:
        date_time = index.date
        date_string = date_time.strftime('%y-%m-%d')
        all_date.append(date_string)
        count = count + 1
        time_list.append(count)
        addconfirm_list.append(int(index.oneday_today_confirm))
    for i in range(count, count + 10):
        future.append(i)

    def logistic_increase_function(t, K, P0):
        # r 0.05/0.55/0.65
        r = 0.08
        t0 = 20
        # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
        exp_value = np.exp(r * (t - t0))
        return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

    #  日期及感染人数
    time_array = np.array(time_list)
    confirm_array = np.array(addconfirm_list)

    # 用最小二乘法估计拟合
    # 现有数据曲线拟合检验
    popt1, pcov1 = curve_fit(logistic_increase_function, time_array, confirm_array)

    # 获取popt里面是拟合系数
    print("K:capacity  P0:initial_value   r:increase_rate   t:time")
    print(popt1)
    # 拟合后预测的P值

    confirm_array_predict = logistic_increase_function(time_array, popt1[0], popt1[1])
    # 未来预测
    future = np.array(future)
    future_predict = logistic_increase_function(future, popt1[0], popt1[1])
    future_predict_list = future_predict.tolist()
    print(future_predict_list)
    future_predict_list = [int(i) for i in future_predict_list]
    print(future_predict_list)
    # 绘图
    # plt.plot(time_array, confirm_array, 's', label="confimed people")
    # plt.plot(time_array, confirm_array_predict, 'r', label='predict people')
    # plt.plot(future, future_predict, 's', label='future predict people')
    # plt.xlabel('time')
    # plt.ylabel('confimed people')
    # plt.legend(loc=0)  # 指定legend的位置右下角
    #
    # print(logistic_increase_function(np.array(28), popt1[0], popt1[1]))
    # print(logistic_increase_function(np.array(29), popt1[0], popt1[1]))
    # plt.show()

    #  近一个月的数据+预测的数据
    month_future_date = all_date[-30:] + ['+' + str(i + 1) for i in range(len(future))]
    month_future_confirm = addconfirm_list[-30:] + future_predict_list
    return month_future_date, month_future_confirm



#  针对上海市疫情发展预测
def predict_sh():
    count = 0
    future = list()
    time_list = list()
    addconfirm_list = list()
    all_date = list()
    shmodel = ShangHaiModel
    shmodel = shmodel.select().order_by(shmodel.lastUpdateTime.asc()).limit()
    for index in shmodel:
        date_time = index.lastUpdateTime
        date_string = date_time.strftime('%y-%m-%d')
        all_date.append(date_string)
        count = count + 1
        time_list.append(count)
        addconfirm_list.append(int(index.sh_confirm))
    for i in range(count, count + 10):
        future.append(i)

    def logistic_increase_function(t, K, P0):
        # r 0.05/0.55/0.65
        r = 0.1
        t0 = 11
        # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
        exp_value = np.exp(r * (t - t0))
        return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

    #  日期及感染人数
    time_array = np.array(time_list)
    confirm_array = np.array(addconfirm_list)

    # 用最小二乘法估计拟合
    # 现有数据曲线拟合检验
    popt1, pcov1 = curve_fit(logistic_increase_function, time_array, confirm_array)

    # 获取popt里面是拟合系数
    print("K:capacity  P0:initial_value   r:increase_rate   t:time")
    print(popt1)
    # 拟合后预测的P值

    confirm_array_predict = logistic_increase_function(time_array, popt1[0], popt1[1])
    # 未来预测
    future = np.array(future)
    future_predict = logistic_increase_function(future, popt1[0], popt1[1])
    future_predict_list = future_predict.tolist()
    print(future_predict_list)
    future_predict_list = [int(i) for i in future_predict_list]
    print(future_predict_list)
    # 绘图
    # plt.plot(time_array, confirm_array, 's', label="confimed people")
    # plt.plot(time_array, confirm_array_predict, 'r', label='predict people')
    # plt.plot(future, future_predict, 's', label='future predict people')
    # plt.xlabel('time')
    # plt.ylabel('confimed people')
    # plt.legend(loc=0)  # 指定legend的位置右下角

    # print(logistic_increase_function(np.array(28), popt1[0], popt1[1]))
    # print(logistic_increase_function(np.array(29), popt1[0], popt1[1]))
    # plt.show()
    #  近一个月的数据+预测的数据
    month_future_date = all_date[-30:] + ['+' + str(i + 1) for i in range(len(future))]
    month_future_confirm = addconfirm_list[-30:] + future_predict_list
    return month_future_date, month_future_confirm



#  针对世界疫情发展预测
def predict_world():
    pass


#  针对重点国家的疫情发展进行预测
#  参数为国家代称
# countries_name = ['us', 'brazil', 'france', 'germany', 'uk', 'russia', 'italy', 'spain']

def predict_maincountries(country_name):
    count = 0
    future = list()
    time_list = list()
    addconfirm_list = list()
    all_date = list()
    tablename = 'maincountries_' + country_name
    maincountriesmodel = MainCountries(0, tablename)
    maincountriesmodel = maincountriesmodel.select().order_by(maincountriesmodel.lastUpdateTime.asc()).limit()
    for index in maincountriesmodel:
        date_time = index.lastUpdateTime
        date_string = date_time.strftime('%y-%m-%d')
        all_date.append(date_string)
        count = count + 1
        time_list.append(count)
        addconfirm_list.append(int(index.confirmedCount))
    for i in range(count+1, count+11):
        future.append(i)

    def logistic_increase_function(t, K, P0):
        # r 0.05/0.55/0.65
        r = 0.008
        t0 = 200
        # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
        exp_value = np.exp(r * (t - t0))
        return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

    #  日期及感染人数
    time_array = np.array(time_list)
    confirm_array = np.array(addconfirm_list)

    # 用最小二乘法估计拟合
    # 现有数据曲线拟合检验
    popt1, pcov1 = curve_fit(logistic_increase_function, time_array, confirm_array)

    # 获取popt里面是拟合系数
    print("K:capacity  P0:initial_value   r:increase_rate   t:time")
    print(popt1)
    # 拟合后预测的P值

    confirm_array_predict = logistic_increase_function(time_array, popt1[0], popt1[1])
    # 未来预测
    future = np.array(future)
    future_predict = logistic_increase_function(future, popt1[0], popt1[1])
    future_predict_list = future_predict.tolist()
    print(future_predict_list)
    future_predict_list = [int(i) for i in future_predict_list]
    print(future_predict_list)
    # 绘图
    # plt.plot(time_array, confirm_array, 's', label="confimed people")
    # plt.plot(time_array, confirm_array_predict, 'r', label='predict people')
    # plt.plot(future, future_predict, 's', label='future predict people')
    # plt.xlabel('time')
    # plt.ylabel('confimed people')
    # plt.legend(loc=0)  # 指定legend的位置右下角
    #
    # print(logistic_increase_function(np.array(28), popt1[0], popt1[1]))
    # print(logistic_increase_function(np.array(29), popt1[0], popt1[1]))
    # plt.show()

    #  近一个月的数据+预测的数据
    month_future_date = all_date[-30:] + ['+'+str(i+1) for i in range(len(future))]
    month_future_confirm = addconfirm_list[-30:] + future_predict_list
    return month_future_date,month_future_confirm



