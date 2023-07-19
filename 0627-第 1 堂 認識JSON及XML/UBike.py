# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
爬蟲分兩種:
1.有整理:json, xml, csv
2.未整理:html, Ajax, 偽裝成Google BOT, 反爬蟲
"""

#json parser

#新北市UBike

import requests
import json

url = "https://data.ntpc.gov.tw/api/datasets/71cd1490-a2df-4198-bef1-318479775e8a/json?size=100"
data = requests.get(url).text #串流轉成文字
#print(data)

bike = json.loads(data)

for row in bike:
    print('站名:',row['sna'])
    print('可借:',row['sbi'])
    print('可停:',row['bemp'])
    print()