# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:27:28 2023

@author: USER
"""

import copy

data = [100,200,300,400] #一維串列
num = copy.copy(data) #淺複製，用於一維串列
data.append(10)
print(num)
print(data)

data2 = [[10,20,30],[1,2,3,4,5,6]]
print(data2[1])
print(data2[0][2])
print(data2[1][4])
print(data2)