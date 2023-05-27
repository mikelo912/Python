# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:17:28 2023

@author: thewh
"""


def total(n1,n2,n3):
    res = 0
    for i in range(n1,n2+1,n3):
        res += i
    return res

print('計算總和')
key = input("按y開始")

while key == 'y':
    start = int(input('輸入起始值'))
    end = int(input('輸入終點值'))
    step = int(input('輸入間隔值'))
    result = total(start, end, step)
    print("總和:", result)
    key = input("按y繼續:")