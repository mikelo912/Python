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
    f = input("請輸入分數，Enter離開:")
    if f == "" :
        break
    if scores.count(f) > 0:
        index = scores.index(f)
        scores.pop(index)
    else:
        print("沒有此分數")    