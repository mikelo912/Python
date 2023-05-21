# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:05:30 2023

@author: thewh
"""

#巴斯卡三角形
'''
1
11
121
1331
以此類推
'''

n = int(input("幾層?"))

data = [1] #設定data陣列，內容給1

for i in range(n):
    print(data)
    plist = [] #設定一個空陣列plist
    plist.append(data[0]) #新增data[0]的值到plist
    for j in range(len(data)-1): #len(data)是抓取data陣列的長度
        plist.append(data[j]+data[j+1])
    plist.append(data[-1])
    data = plist #將plist的資料帶入data
