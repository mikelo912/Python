# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:21:36 2023

@author: USER
"""

data = [1,2,3,4,5]
num = []
for i in data:
    num.append(i)
print(num)

data[0]=100
print(num)
print(data)