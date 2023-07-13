# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:03:45 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
header={
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
data = requests.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

soup = BeautifulSoup(data,'html.parser')

rate = soup.find('table')
allRate = rate.find('tbody')
trs = allRate.find_all('tr') #抓取每一行的資料

for item in trs:
    tds = item.find_all('td')
    #print(tds)
    
    currency = tds[0].text.strip()
    currency = currency.split() #strip()->去除前後空白
    print('幣別:',currency[0],currency[1])
    print('現金匯率')
    print('本行買入:',tds[1].text.strip())
    print('本行賣出:',tds[2].text.strip())
    print('即期匯率')
    print('本行買入:',tds[3].text.strip())
    print('本行賣出:',tds[4].text.strip())
    print()
    
    
    
#作業: 到玉山銀行網站抓取匯率資料