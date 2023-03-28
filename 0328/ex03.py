# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:09:41 2023

@author: USER
"""

fruits = ['香蕉', '蘋果', '香瓜', '西瓜']
while True:
    print("目前水果有:",fruits)
    f = input("請輸入欲刪除的水果，Enter離開:")
    if f == "" :
        break
    if fruits.count(f) > 0:
        fruits.remove(f)
    else:
        print("沒有此水果")
 
'''
作業1
scores = [100,60,70,80,99,100,66]
由使用者輸入分數後，找到就移除(限用pop)
找不到時要顯示找不到

作業2
由使用者分別輸入六個數字，並放入串列中
請用巢狀迴圈進行由大至小排序，並印出結果
'''