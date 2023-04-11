# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#巴斯卡三角形
n = int(input("幾層?"))
data = [1]
for i in range(n):
    print(data) #先印出data串列
    plist = []
    plist.append(data[0]) 
    for i in range(len(data)-1):
        plist.append(data[i]+data[i+1]) #新增data[i]+data[i+1]到plist串列
    plist.append(data[-1]) #抓data串列的最後一個值
    data = plist
