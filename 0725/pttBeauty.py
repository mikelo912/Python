# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:41:01 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc/bbs/Beauty/index.html"

header = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
"Cookie":"over18=1"
}

soup = BeautifulSoup()
for i in range(1,7):
    if i > 1:
        uppage = soup.find_all('a', class_="btn wide")
        URL = 'https://www.ptt.cc' + uppage[1].get('href')
    
    data = requests.get(URL, headers=header).text #將抓到的資料轉成文字
    #print(data)
    
    soup = BeautifulSoup(data,'html.parser')
    beauty = soup.find_all('div', class_='r-ent')
    
    for row in beauty:
        a = row.find('a')
        if not (a == None): #如果文章未被刪除，表示有標籤a的資料
            link = 'https://www.ptt.cc' + row.find('a').get('href')
            title = row.find('a').text
            print(title)
            print(link)
            print()