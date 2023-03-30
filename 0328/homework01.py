# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:29:33 2023

@author: USER
"""

'''
作業1
scores = [100,60,70,80,99,100,66]
由使用者輸入分數後，找到就移除(限用pop)
找不到時要顯示找不到
'''

scores = [100,60,70,80,99,100,66]

while True:
    print("目前有這些分數:",scores)
    f = int(input("請輸入欲刪除之分數，輸入-1離開:"))
    if f == -1 :
        break
    if scores.count(f) > 0:
        index = scores.index(f)
        start = 0
        
        for i in range(scores.count(f)):
            index = scores.index(f,start)
            scores.pop(index)
            start = index + 1
    else:
        print("沒有此分數")
