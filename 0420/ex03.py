# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:40:54 2023

@author: USER
"""

data = [100,80,60,70]

try:
    ans = 100 / 0
    print(data[0])
    print(data[2])
    print(data[10])
    
except IndexError as ex:
    print('超過索引值')
except:
    print('其他error')
    
print('程式執行完畢')