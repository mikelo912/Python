# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:58:54 2023

@author: USER
"""

#作業: 到台灣彩券抓開獎結果

import requests
from bs4 import BeautifulSoup

header = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
    
URL = 'https://www.taiwanlottery.com.tw/index_new.aspx'

bingo = requests.get(URL,headers=header).text
#print(bingo)
parser = BeautifulSoup(bingo,'html.parser') #建立網頁解析器
bingoData = parser.find('div',class_="contents_box01")

YBall = bingoData.find_all('div',class_='ball_tx ball_yellow')
RBall = bingoData.find('div',class_='ball_red').text

print("BINGO BINGO")
print("開出獎號:")
for n in YBall:
    print(n.text)
print("超級獎號:",RBall)

print('-'*30)
print('雙贏彩')

twowin = parser.find('div',class_='contents_box06')
BBall = twowin.find_all('div',class_='ball_tx ball_blue')
BBall = BBall[12:]
print("開出獎號:")
for n in BBall:
    print(n.text)

print('-'*30)
print('威力彩')

lottery = parser.find_all('div',class_='contents_box02')
Power = lottery[0].find_all('div',class_='ball_tx ball_green')
Power = Power[6:]
Power_Red = lottery[0].find('div',class_='ball_red')
print("開出獎號:")
for n in Power:
    print(n.text)
print("第二區:",Power_Red.text)

print('-'*30)
print('大樂透')

BigLottery = lottery[2].find_all('div',class_='ball_tx ball_yellow')
BigLottery = BigLottery[6:]
BigLottery_Red = lottery[2].find('div',class_='ball_red')
print("開出獎號:")
for n in BigLottery:
    print(n.text)
print("特別號:",BigLottery_Red.text)