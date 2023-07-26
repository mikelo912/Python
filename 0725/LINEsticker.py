# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:03:45 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import json
import urllib.request #抓取圖片的函式庫

URL = 'https://store.line.me/stickershop/product/26224/zh-Hant'

header = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

data = requests.get(URL,headers=header).text
soup = BeautifulSoup(data,'html.parser')
li = soup.find_all('li', class_='mdCMN09Li FnStickerPreviewItem popup-sticker')
#print(li[0])

i=1
for row in li:
    img = row.get('data-preview')
    sticker = json.loads(img)
    urllib.request.urlretrieve(sticker['staticUrl'],str(i)+'.png') #下載圖片
    i+=1