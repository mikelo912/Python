# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:07:57 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://tw.buy.yahoo.com/search/product"
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

param = {}
p = input('請輸入想要搜尋的商品:')
param['p'] = p
    
shopping = requests.get(url, headers = header, params = param).text
soup = BeautifulSoup(shopping,'html.parser')
#print(soup)

goods = soup.find_all('a', class_ = 'sc-1drl28c-1 hcbDur')
for item in goods:
    goodsName = item.find('span', class_ = 'sc-1d7r8jg-0 sc-dp9751-0 sc-1drl28c-5 kAwLVo fSJeRk bzFZqJ')
    #goodsName = item.find('img').get('alt') #第二種寫法
    URL = item.get('href')
    allPrice = item.find('div', class_ = 'sc-1ap2njs-0 dPpkAj')
    Price = allPrice.find_all('span', class_ = 'eCzBYn')
    print(goodsName.text)
    #print(goodsName) #第二種寫法
    
    #print('特價:', Price[0].text)
    
    #將價格的$及,去掉
    intPrice = Price[0].text.replace('$','')
    intPrice = intPrice.replace(',','')
    print('特價:', intPrice)
    
    if len(Price) == 2:
        intPrice2 = Price[1].text.replace('$','')
        intPrice2 = intPrice.replace(',','')
        #print('原價:', Price[1].text)
        print('原價:', intPrice2)
            
    print(URL)
    print()