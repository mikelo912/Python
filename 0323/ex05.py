# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:23:22 2023

@author: USER
"""

students=list()
scores=[]
while True:
    name = input("搜尋學生姓名q離開:")
    if name == "q":
        break
    if students.count(name) == 0:
        num = int(input("輸入分數:"))
        students.append(name)
        scores.append(num)
    else:
        index = students.index(name)
        sco = scores[index]
        print(name,"的分數:",sco)