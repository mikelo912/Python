# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 08:22:16 2023

@author: s9571
"""

import requests #HTTP函式庫，可向網站發送HTTP請求並得到回應
#from bs4 import BeautifulSoup #分析網頁的HTML與XML文件，並將分析結果轉換成tag的型態

web = requests.get('https://water.taiwanstat.com/')  # 使用 get 方法
web.encoding = 'utf-8'
print(web.text)    # 讀取並印出 text 屬性