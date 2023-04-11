# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:29:53 2023

@author: USER
"""

scores = [60,70,65,100,91,88,65,81]
search = 65
start = 0

for i in range(scores.count(search)): #計算search的值在scores裡有幾個
    index = scores.index(search,start+1) #使用index()方法查找scores列表中從start+1位置開始的第一個匹配項的索引
    print("索引值:",index)
    start = index + 1
