# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:49:08 2023

@author: USER
"""

number = [[10,20,30],[1,2],[2,3,4,5,6]]
print(number[1][0])
for item in number:
    for i in item:
        print(i,end=",")
    print()