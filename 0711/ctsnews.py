# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:53:36 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://news.cts.com.tw/money/index.html'
header={
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
data = requests.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

soup = BeautifulSoup(data,'html.parser')
#print(soup)

money = soup.find(id='newslist-top')
allNews = money.find_all('a')
for items in allNews:
    title = items.get('title')
    link = items.get('href')
    
    img = items.find('img') #抓img標籤內容
    if not img == None:
        img_url = img.get('data-src')
    else:
        print('沒有縮圖\n'+'-'*30)
        #continue
    
    print(link)
    print(title)
    print(img_url,'\n')