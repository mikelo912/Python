# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 00:16:15 2023

@author: s9571
"""

import requests
import json
import csv

url = 'https://www.thsrc.com.tw/TimeTable/Search'
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
param = {'SearchType': 'S',
'Lang': 'TW',
'StartStation': 'NanGang',
'EndStation': 'ZuoYing',
'OutWardSearchDate': '2023/07/20',
'OutWardSearchTime': '09:00',
'ReturnSearchDate': '2023/07/20',
'ReturnSearchTime': '09:00'}

thrs = requests.post(url,headers=header,data=param).text #將抓取的資料轉成字串
data = json.loads(thrs)
#print(data)

THRS = data['data']['DepartureTable']['TrainItem'] #透過關鍵字抓想要的資料
#print(THRS)

number = list()
starttime = list()
endtime = list()
duration = list()

for item in THRS:
    number.append(item['TrainNumber'])
    starttime.append(item['DepartureTime'])
    duration.append(item['Duration'])
    endtime.append(item['DestinationTime'])
    
fileName = 'THRS.csv'
with open(fileName,'w',newline='') as fO: #參數w是覆寫
    csvWrite = csv.writer(fO)
    csvWrite.writerow(['車次','出發時間','旅行時間','抵達時間'])
    
    for i in range(len(number)):
        csvWrite.writerow([number[i],starttime[i],duration[i],endtime[i]])
    print('存檔完成')