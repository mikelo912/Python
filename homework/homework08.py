# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:49:03 2023

@author: thewh
"""

#題目：印出9*9乘法表。

for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i,j,i*j))