# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
header={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
data = requests.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

soup = BeautifulSoup(data,'html.parser')
#print(soup)

rate = soup.find('table') #在整個網頁內抓表格內容
trs = rate.find_all('tr') #抓取每一行的資料
trs = trs[2:]

#print(trs[0])

for item in trs:
    tds = item.find_all('td')
    # print(len(tds))
    # print(tds[0])
    # break

    if len(tds) == 7:
        currency = tds[0].text.strip().split()
        print(currency[0],currency[1])
        print(tds[-3])
        print('即期匯率',tds[-3].text)
        print('網銀/App優惠',tds[-2].text)
        print('現金匯率',tds[-1].text)
        print('-'*30)
        # break