# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:50:30 2023

@author: USER
"""

data = [100,80,60,70]

try:
    print(data(1))
    ans = 100 / 0
    print(data[0])
    print(data[2])
    print(data[10])
    
except Exception as ex:
    print(ex)    
    
print('程式執行完畢')