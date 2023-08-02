# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:46:45 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://member.lccnet.com.tw/%E5%AD%B8%E7%BF%92%E8%A9%95%E5%83%B9Partial?key=105670139"

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
data = requests.get(url,headers=header).text    
#print(data)    
soup = BeautifulSoup(data,'html.parser')

intag = soup.find_all('input')
lastless = intag[-1].get('value')
lastnum = intag[-2].get('value')
print(lastless)
print(lastnum)

params = {
'關鍵字': '105670139',
'評價分數': '10',
'Item加強項目s[0].Value': 'false',
'Item加強項目s[0].Key': '1',
'Item加強項目s[1].Value': 'false',
'Item加強項目s[1].Key': '2',
'Item加強項目s[2].Value': 'false',
'Item加強項目s[2].Key': '3',
'Item加強項目s[3].Value': 'false',
'Item加強項目s[3].Key': '4',
'Item加強項目s[4].Value': 'false',
'Item加強項目s[4].Key': '5',
'Item加強項目s[5].Value': 'false',
'Item加強項目s[5].Key': '99',
'Is與我聯絡': 'false',
'授課堂數': lastnum,
'班級編號': lastless
    }

url = 'https://member.lccnet.com.tw/signout/LearningRecord.aspx'
data = requests.post(url,data=params,headers=header).text  