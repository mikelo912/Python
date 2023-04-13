# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:04:45 2023

@author: thewh
"""

def circle(r):
    area = r * r * 3.14
    per = 2 * r * 3.14
    
    return area,per #回傳兩個值用元組放

ci = circle(5)
a,p = circle(12) #把回傳值給a跟p

print(ci)
print(a)
print(p)