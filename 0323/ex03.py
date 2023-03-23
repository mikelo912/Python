# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:55:19 2023

@author: USER
"""

scores = list()
while True:
    number = int(input("輸入分數-1離開:"))
    if number == -1:
        break
    scores.append(number) #append可以將物件依序加入串列
print(scores)