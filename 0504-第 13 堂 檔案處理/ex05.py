# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:41:13 2023

@author: USER
"""

fn = "file02.txt"

with open(fn, encoding='utf-8') as fObj:
    #data = fOBJ.readline() #只讀入一行
    datas = fObj.readlines() #每次讀一行並存入list中
    
print(datas)
print('-'*30)
print(datas[2])
print('-'*30)

for line in datas:
    print(line.strip()) #去除前後空白