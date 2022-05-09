import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DB.chinaday import addchinaday
from DB.provinces import addprovinces
from DB.worldcountries import addcountries


def wangyi():
    url_api = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=330344037731'
    driver_path = '../chromedriver/mac64/chromedriver'
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    # 开启静默模式
    browser = webdriver.Chrome(driver_path,chrome_options=chrome_options)
    browser.get(url_api)
    raw_json_data = json.loads(browser.find_element_by_tag_name('body').text)['data']
    return raw_json_data


def chinatoday():   #   累计数据和今日增减数据
    raw_json_data = wangyi()
    lastUpdateTime = raw_json_data['lastUpdateTime']
    chinatotal_json = raw_json_data['chinaTotal']
    chinatotal_confirm = chinatotal_json['total']['confirm']  # 累计确诊
    chinatotal_suspect = chinatotal_json['total']['suspect']  # 累计疑似
    chinatotal_heal = chinatotal_json['total']['heal']     # 累计治愈
    chinatotal_dead = chinatotal_json['total']['dead']   # 累计死亡
    chinatotal_severe = chinatotal_json['total']['severe']     # 现存重症
    chinatotal_input = chinatotal_json['total']['input']   # 累计境外输入
    chinatotal_nosymptom = chinatotal_json['extData']['noSymptom']   # 累计无症状

    chinaadd_json = raw_json_data['chinaTotal']['today']
    chinaadd_confirm = chinaadd_json['confirm']
    chinaadd_suspect = chinaadd_json['suspect']
    chinaadd_heal = chinaadd_json['heal']
    chinaadd_dead = chinaadd_json['dead']
    chinaadd_storeConfirm = chinaadd_json['storeConfirm']
    chinaadd_severe = chinaadd_json['severe']
    chinaadd_input = chinaadd_json['input']
    extData = ''
    #  将数据写入数据库
    addchinaday(lastUpdateTime, extData, lastUpdateTime, chinaadd_confirm, chinaadd_suspect, chinaadd_heal,
                chinaadd_dead, chinaadd_storeConfirm, chinaadd_severe, chinaadd_input,
                chinatotal_confirm, chinatotal_suspect, chinatotal_heal, chinatotal_dead,
                chinatotal_severe, chinatotal_input)



def chinaDayList(raw_json_data):   #   近两个月信息

    chinaDayList_json = raw_json_data['chinaDayList']
    for oneday in chinaDayList_json:
        date = oneday['date']
        extData = oneday['extData']
        lastUpdateTime = oneday['lastUpdateTime']
        oneday_today_confirm = oneday['today']['confirm']
        oneday_today_suspect = oneday['today']['suspect']
        oneday_today_heal = oneday['today']['heal']
        oneday_today_dead = oneday['today']['dead']
        oneday_today_storeConfirm = oneday['today']['storeConfirm']
        oneday_today_severe = oneday['today']['severe']
        oneday_today_input = oneday['today']['input']
        oneday_total_confirm = oneday['total']['confirm']
        oneday_total_suspect = oneday['total']['suspect']
        oneday_total_heal = oneday['total']['heal']
        oneday_total_dead = oneday['total']['dead']
        oneday_total_severe = oneday['total']['severe']
        oneday_total_input = oneday['total']['input']

        #  将数据写入数据库
        addchinaday(date, extData, lastUpdateTime, oneday_today_confirm, oneday_today_suspect, oneday_today_heal,
                        oneday_today_dead, oneday_today_storeConfirm, oneday_today_severe, oneday_today_input,
                        oneday_total_confirm, oneday_total_suspect, oneday_total_heal, oneday_total_dead,
                        oneday_total_severe, oneday_total_input)

    

def worldinfo():   #   世界各地信息
    raw_json_data = wangyi()
    lastUpdateTime = raw_json_data['lastUpdateTime']
    worldinfo_dict = dict()
    provinceinfo_dict = dict()
    lastUpdateTime  =''
    areatree_json = raw_json_data['areaTree']
    for country in areatree_json:
        if country['name'] == '中国':
            lastUpdateTime = country['lastUpdateTime']
            for province in country['children']:
                province_name = province['name']
                province_today_confirm = province['today']['confirm']
                province_today_suspect = province['today']['suspect']
                province_today_heal = province['today']['heal']
                province_today_dead = province['today']['dead']
                province_today_storeConfirm = province['today']['storeConfirm']
                province_today_severe = province['today']['severe']
                #  total
                province_total_confirm = province['total']['confirm']
                province_total_suspect = province['total']['suspect']
                province_total_heal = province['total']['heal']
                province_total_dead = province['total']['dead']
                province_total_severe = province['total']['severe']
                province_total_input = province['total']['input']
                provinceinfo_dict[province_name] = [province_today_confirm,province_today_suspect,province_today_heal,province_today_dead,province_today_storeConfirm,province_today_severe,province_total_confirm,province_total_suspect,province_total_heal,province_total_dead,province_total_severe,province_total_input]
            #   写入数据库中
            addprovinces(lastUpdateTime, provinceinfo_dict)
        country_name = country['name']
        country_today_confirm = country['today']['confirm']
        country_today_suspect = country['today']['suspect']
        country_today_heal = country['today']['heal']
        country_today_dead = country['today']['dead']
        country_today_storeConfirm = country['today']['storeConfirm']
        country_today_severe = country['today']['severe']   
        #  total
        country_total_confirm = country['total']['confirm']
        country_total_suspect = country['total']['suspect']
        country_total_heal = country['total']['heal']
        country_total_dead = country['total']['dead']
        country_total_severe = country['total']['severe']
        try:
            country_total_input = country['total']['input']
        except:
            country_total_input = 0
        worldinfo_dict[country_name] = [country_today_confirm,country_today_suspect,country_today_heal,country_today_dead,country_today_storeConfirm,country_today_severe,country_total_confirm,country_total_suspect,country_total_heal,country_total_dead,country_total_severe,country_total_input]
    addcountries(lastUpdateTime, worldinfo_dict)
