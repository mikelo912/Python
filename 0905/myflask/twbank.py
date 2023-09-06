# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:03:45 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup


def getRate():
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
    trs = rate.find_all('tr') #抓取每一行的資料
    trs = trs[2:]
    
    rate = list()
    
    #在每行資料中抓每一格資料
    for item in trs:
        tds = item.find_all('td')
        #print(tds)
        
        currency = tds[0].text.strip()
        currency = currency.split() #strip()->去除前後空白
        # print(currency[0],currency[1])
        # print(tds[1].text.strip())
        # print(tds[2].text.strip())
        # print(tds[3].text.strip())
        # print(tds[4].text.strip())
        # print()
    
        temp = list()
        temp.append(currency[0])
        temp.append(tds[1].text.strip())
        temp.append(tds[2].text.strip())
        rate.append(temp)
    
    return rate
    
#作業: 到玉山銀行網站抓取匯率資料