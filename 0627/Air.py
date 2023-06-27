# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:38:30 2023

@author: USER
"""

import requests
import json

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
data = requests.get(url).text #串流轉成文字
print(data)

air = json.loads(data)

air = air['records']

for row in air:
    print('站名:',row['sitename'])
    print('縣市:',row['county'])
    print('AQI:',row['aqi'])
    
    aqi = int(row['aqi'])
    
    if aqi < 50:
        print('空氣品質:良好')
    elif aqi < 100:
        print('空氣品質:普通')
    else:
        print('空氣品質:危害')
            
    print()