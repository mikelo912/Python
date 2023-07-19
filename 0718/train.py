# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 21:55:59 2023

@author: s9571
"""

import requests
from bs4 import BeautifulSoup

url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation"
header = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
param = {
    "_csrf": "0ceee543-3817-4461-9462-b18ecb0dc0ef",
    "rideDate": "2023/07/19",
    "station": "3300-臺中"
    }

data = requests.post(url,headers=header,data=param).text #POST方法的參數是data，GET方法是params
#print(data)
soup = BeautifulSoup(data,'html.parser')

direct = soup.find(id='tab1') #順行
retrograde = soup.find(id='tab2') #逆行
direct_tr = direct.find_all('tr')
retrograde_tr = retrograde.find_all('tr')
direct_tr = direct_tr[1:] #從索引值1之後開始抓
retrograde_tr = retrograde_tr[1:]

print('順行')
for item in direct_tr:
    tds = item.find_all('td')
    print('車種車次',tds[0].text.strip().replace('\n','')) #將斷行符號以空白取代
    print('時間',tds[1].text.strip())
    print('終點站',tds[2].text.strip())
    print('目前狀態',tds[4].text.strip())
    print()
    
print('逆行')
for item in retrograde_tr:
    tds = item.find_all('td')
    route = tds[0].text.strip().split()
    print('車種車次',route[0],route[1])
    print('起訖站',route[3],route[4],route[5])
    print('時間',tds[1].text.strip())
    print('終點站',tds[2].text.strip())
    print('目前狀態',tds[4].text.strip())
    print()