# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:29:28 2023

@author: USER
"""

import requests
url = 'https://images.chinatimes.com/newsphoto/2023-05-07/1024/20230507003260.jpg'
data = requests.get(url,stream=True)
with open('lcc.jpg','wb') as f:
    for block in data.iter_content(1024): 
    #iter_content()讀取網頁裡的資料，1024為檔案大小,1KB
        if not block:
            break
        f.write(block)