# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 06:53:35 2023

@author: s9571
"""

import requests
import json

url = 'https://24h.pchome.com.tw/onsale/'
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

pchome = requests.get(url, headers=header).text
#data = json.loads(pchome)
#onsale = data['OnsaleJson']
#print(onsale)

# for item in onsale:
#     if item['BlockId'] == 1:
#         print("3C")
#     elif item['BlockId'] == 2:
#         print("家電")
#     elif item['BlockId'] == 3:
#         print("日常")