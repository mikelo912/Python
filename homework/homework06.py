# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:16:19 2023

@author: thewh
"""

'''
題目：印出費氏數列（Fibonacci sequence），又稱黃金分割數列，
指的是這樣一個數列：0、1、1、2、3、5、8、13、21、34、……。
'''

leng = int(input('請輸入費式數列長度:'))
F_seq = [0,1]

for i in range(2,leng):
    F_seq.append(F_seq[i-2] + F_seq[i-1]) 
    
print(F_seq)