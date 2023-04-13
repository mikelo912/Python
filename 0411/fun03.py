# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:32:13 2023

@author: thewh
"""

def bigorsmall(x,y):

    if x>y:
        return x
    else:
        return y
    
#print(bigorsmall())

x = int(input('輸入x:'))
y = int(input('輸入y:'))

big = bigorsmall(x,y)
print("最大值:", big)


