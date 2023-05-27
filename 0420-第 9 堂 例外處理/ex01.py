# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:54:40 2023

@author: USER
"""

data = [100,80,60,70]

try:
    ans = 100 / 0
    
    print(data[0])
    print(data[2])
    print(data[10])
    
except (IndexError, ZeroDivisionError) as ex:
    print(ex)
    
print('程式執行完畢')