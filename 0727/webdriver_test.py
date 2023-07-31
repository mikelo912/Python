# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 01:56:02 2023

@author: s9571
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driverpath = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(driverpath)

url = "https://tw.buy.yahoo.com/search/product?p=iphone"
driver.implicitly_wait(3) #背景等待時間3秒
driver.get(url) #執行chrome

height = 800
for i in range(5):
    driver.execute_script('window.scrollTo(0,{})'.format(height)) #網頁卷軸往下移動
    time.sleep(1)
    height += 800
    
soup = BeautifulSoup(driver.page_source,'html.parser')
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