# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'
header={
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
data = requests.get(url,headers=header).text
soup = BeautifulSoup(data,'html.parser')
news = soup.find(id='NewsList')

#print(news)

allNews = news.find_all('h3') #抓所有新聞的h3標籤內容
for item in allNews:
    link = item.find('a').get('href') #抓超連結
    
    #幫不完整的網址補上前面的http...
    if not('http' in link):
        link = 'https://www.setn.com/' + link
    
    title = item.find('a').text #抓標題
    print(link)
    print(title,'\n')