# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:01:25 2023

@author: USER
"""

import requests
import json

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
data = requests.get(url).text #串流轉成文字
#print(data)

air = json.loads(data)
air = air['records']

county = {}
for row in air:
    area = county.get(row['county'])
    #找不到縣市就新增
    if area == None:
        temp = list()
        sitedict = dict()
        sitedict['sitename'] = row['sitename']
        sitedict['aqi'] = row['aqi']
        temp.append(sitedict)
        county[row['county']] = temp
    else:
        sitedict = dict()
        sitedict['sitename'] = row['sitename']
        sitedict['aqi'] = row['aqi']
        area.append(sitedict)

print(county)


#作業:顯示某個縣市有哪些測站
coun = input('請輸入欲查詢的縣市(台北市請打臺北市，依此類推):')
for i in range(len(county[coun])):
    print(county[coun][i]['sitename'])