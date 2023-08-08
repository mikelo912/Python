# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 16:34:10 2023

@author: USER
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="body strikout">Test</p>','html.parser')
p = soup.find('p',class_='strikout').text
#css選擇器，p.body.strikout表示搜尋p裡面class為body以及strikout的資料，格式為串列
p_tag = soup.select('p.body.strikout')[0].text
print(p)
print(p_tag)

soup = BeautifulSoup('<p id="news">新聞</p>','html.parser')
news = soup.find(id='news').text
print(news)
cssnews = soup.select('#news')[0].text #id在css要在前面加#
print(cssnews)