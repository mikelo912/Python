# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 06:53:35 2023

@author: s9571
"""

import requests
import json

url = 'https://24h.pchome.com.tw/onsale/v5/data/data.json'
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

pchome = requests.get(url, headers=header).text
data = json.loads(pchome)
onsale = data['OnsaleJson']
#print(onsale)

for item in onsale:
    if item['BlockId'] == 1:
        print("3C")
    elif item['BlockId'] == 2:
        print("家電")
    elif item['BlockId'] == 3:
        print("日常")
    else:
        continue
    
    goods = item['Nodes']
    for p in goods:
        URL = 'https:' + p['Link']['Url']
        onSale = p['Link']['Text2']
        price = p['Link']['Text6']
        #到網站尚未讀取商品圖片的預設圖片去找background-image，可知網域名稱
        Img = 'https://fs-c.ecimg.tw' + p['Img']['Src']
        Title = p['Img']['Title']
        print(Title)
        print(Img)
        print(URL)
        print('特價:',onSale,'元')
        print('原價:',price,'元')
        print()