# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:07:52 2023

@author: s9571
"""

import requests
import json
import time

URL = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results'
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
param = {'q':'可口可樂','page':'2','sort':'sale/dc'}


    


pchome = requests.get(URL, headers=header,params=param).text
data = json.loads(pchome)

allgoods = data['prods']
for item in allgoods:
    name = item['name']
    describe = item['describe']
    pic = 'https://cs-a.ecimg.tw' + item['picB']
    price = item['price']
    URL = 'https://24h.pchome.com.tw/prod/' + item['Id']
    
    print(name)
    print(describe)
    print('網路價:',price,'元')
    print(pic)
    print(URL)
    print()
print('-'*30)

time.sleep(2)