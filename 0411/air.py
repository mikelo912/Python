# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 09:33:30 2023

@author: thewh
"""
import requests
import json

url="https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
data = requests.get(url).text #將網址的內容轉成文字檔，字典型態

air = json.loads(data)

items = air['records']

for row in items: 
    #print(row)
    #print()
    print(row['sitename'])