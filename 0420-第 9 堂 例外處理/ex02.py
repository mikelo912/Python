# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:54:40 2023

@author: USER
"""

data = [100,80,60,70]

try:
    print(data[0])
    print(data[2])
    print(data[10])
    ans = 100 / 0
    
except IndexError as ex:
    print('超過索引值')
except ZeroDivisionError as ex:
    print('不可以除以0')
    
print('程式執行完畢')