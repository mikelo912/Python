# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:40:21 2023

@author: USER
"""

for i in range(1,10):
    for y in range(2,10):
        if i*y >= 18:
            break
        print(i,"*",y,"=",i*y)

print("程式執行完畢")