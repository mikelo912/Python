# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:39:18 2023

@author: thewh
"""

import os

myDir = "lcc"
if os.path.exists(myDir): #判斷有沒有資料夾存在
    print('資料夾已存在')
    os.rmdir(myDir)
    print('資料夾已刪除')
else:
    os.mkdir(myDir)
    print('已建立資料夾')