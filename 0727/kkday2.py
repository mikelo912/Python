# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 04:47:10 2023

@author: s9571
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driverpath = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(driverpath)

url = "https://www.kkday.com/zh-tw/area_api/ajax_get_recommend_top_products?areaCode=A01-001-00020"
driver.implicitly_wait(3) #背景等待時間3秒
driver.get(url) #執行chrome

data = driver.page_source
print(data)