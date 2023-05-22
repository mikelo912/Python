# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:49:03 2023

@author: thewh
"""

#題目：印出9*9乘法表。

#以欄表示一個數字的倍數，i為第二個數字
for i in range(1,10):
    #j為第一個數字，先印出第i列
    for j in range(2,10):
        print('{}x{}={}'.format(j,i,i*j),end='\t')
    print()