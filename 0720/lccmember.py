# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:39:48 2023

@author: s9571
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://member.lccnet.com.tw/'
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'Cookie':
'__RequestVerificationToken=fPv5eQ3MEns6yE2vfOu-RwXORmahTk1gy0OoXDjDUsapFiFnSMixWEgbJykMdGwJ3CGDc7tHWCt7AuKXEhNvRBT324QxOnm-mNtPhDSnGz01'}
param = {'Account': '105670139',
'Password': 'A125218125',
'RememberMe': 'false',
'__RequestVerificationToken': 'nz8KeXjkzVHfxWLLoOLgVjEAUAeCrS-e4bkS_bbC8YxwcS5-qGHZnDUG5zc_OTFZ-GVpW4PkZ9m3Xfyr8Fl5Yn_qkwHCraz0WtiBVve-jOI1'}

session_requests = requests.session() #建立一個session連線的方法
content = session_requests.post(URL, headers=header, data=param).text
#print(content)

URL2 = 'https://member.lccnet.com.tw/Booking'
less = session_requests.get(URL2).text
#print(less)

soup = BeautifulSoup(less,'html.parser')
main = soup.find('ul',class_ = 'courseListWrapper')
allli = main.find_all('li')
print(allli[0])

#作業1:把已登記的課程抓出來
#作業2:簽退