# EpiMoni

# 注意：
项目的启动命令为python manage.py runserver 2>&1 &</br>
疫情数据采集器的启动命令为python spidermain.py 2>&1 &</br>
爬虫会在每天凌晨1:30完成当日最新数据的采集</br>

## 简介
该项目是新冠疫情的实时监测系统，目的是实时监测全国和世界各地疫情的发展情况。

## 项目架构
Flask + Mysql + Layuimini + Bootstrap + AdminLTE + Logistic（预测算法）

## 系统截图
- 登录页
![](http://oh0ra6igz.bkt.clouddn.com/0ot1s.jpg)

- 首页
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig1.png)

- 全国疫情地图  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig2.png)  

- 全球疫情地图  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig3.png)

- 全球疫情区域分析  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig4.png)

- 重点国家疫情排行榜  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig5.png)

- 重点国家疫情趋势分析  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig6.png)

- 上海市疫情状况分析  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig7.png)

- 预测页面  
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig8.png)

- 上海市未來10天疫情预测 
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig9.png)

- 德國未來10天疫情预测 
![](https://github.com/lxyeternal/EpiMoni/blob/main/img/fig10.png)


## 第三方依赖
- peewee
- pymysql
- flask
- flask-script
- flask-wtf
- flask-login


## 环境配置
- Python3.7

### 第三方依赖安装
```
pip3 install -r requirements.txt

```
### 系统参数配置
1. 编辑`config.py`， 修改SECRET_KEY及MySQL数据库相关参数
```
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret'
DB_HOST = '127.0.0.1'
DB_USER = 'foobar'
DB_PASSWD = 'foobar'
DB_DATABASE = 'foobar'
```

2. 编辑log-app.conf，修改日志路径
```
args=('/path/to/log/flask-rest-sample.log','a','utf8')
```

### 数据库初始化
1. 自动建表
直接运行`python3 models.py`

2. 插入管理员用户（默认admin/admin)
```
INSERT INTO `user` (`id`, `username`, `password`, `fullname`, `email`, `phone`, `status`)
VALUES
	(1, 'admin', 'pbkdf2:sha1:1000$Km1vdx3W$9aa07d3b79ab88aae53e45d26d0d4d4e097a6cd3', '管理员', 'admin@admin.com', '18612341234', 1);
```

### 启动应用
```
nohup ./manage.py runserver 2>&1 &
或
./run_app_dev.py (仅限测试)
```


## 项目目录结构
### controller : 所有的功能具体实现
每一个功能新建一个py文件
1.     indexdata: 加载首页展示所需要数据的代码
2.     maincountries: 加载重点国家疫情趋势页面所需数据的代码
3.     nationmap:  加载中国疫情热力图页面所需数据的代码
4.     worldmap: 加载中国疫情热力图页面所需数据的代码
5.     opshnews: 上海市疫情分析页面中疫情消息表单中所需要的数据
6.     rankcountry: 加载重点国家疫情排行榜页面所需要数据的代码
7.     shanghai: 加载上海市页面所需数据的代码
8.   predict：加载疫情预测页面所需的数据（根据历史数据实时预测）
### public : 后端程序运行入口
1.     main.py : 程序入口，包含每一个页面蓝图
#### Main:路由
1.     view.py : 所有的路由，代码里面注释了每个路由的意思
### base : 数据库元模型
### model : 数据库各表对应的具体访问模型
model与数据库表一一对应，数据库中有各字段的说明
1.     ChinaDayModel.py : 国内每日疫情统计数据表模型
2.     ContinentsModel.py : 世界各大洲每日的疫情数据表模型
3.     MainCountries.py : 重点国家疫情数据的表模型
4.     NewsModel.py : 上海市每日最新疫情消息的表模型
5.     ProvinceModel.py : 各省市的每日疫情数据的表模型
6.     ShangHaiAeraModel.py : 上海市各区疫情数据的表模型
7.     ShangHaiModel.py : 上海市总体统计数据的表模型
8.     WorldCountriesModel.py : 世界各个国家疫情数据的表模型
9.     MainCountries.py : 重点国家疫情数据的表模型
10.     UserModel.py：用户表模型
3.     response.py : 前后端数据交互统一格式
### config : 项目后端的配置文件
1.     config.py : 数据库，服务等详细配置文件
2.     log-app.conf : 程序运行日志配置
### logs : 程序运行日志保存位置
### DB: 将采集的数据写入对应表的功能文件（简单来说就是插数据）
1.     chinaday.py : 插中国疫情统计数据
2.     continents.py : 插各洲每日统计数据
3.     maincountries.py : 插8个主要国家疫情统计数据
4.     dbshanghai.py : 插上海每日统计数据
5.     provinces.py : 插各省直辖市疫情统计数据
6.     shaera.conf : 插上海各区每日统计数据
7.     shanghainews.py : 插上海每日新闻数据
8.     continents.conf : 各洲每日统计数据
9.     addcountries.py： 插世界各国的数据

### Templates:所有的前端页面模板
1.     base.html:所有页面的左栏
2.     index.html:首页
3.     predict.html:预测页面
4.     nation_map.html: 全国疫情地图
5.     maincity.html: 上海市疫情状况分析
6.     global_map.html: 全球疫情地图
7.     global_region.html：全球疫情区域分析
8.     rankmaincountry.html: 重点国家疫情排行榜
9.     trendmaincountry.html: 重点国家疫情趋势分析

