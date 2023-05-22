# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:15:21 2023

@author: USER
"""

print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,2)))
print('-'*30)

#加法總和
num = int(input("請輸入整數："))
total = 0
for i in range(num): #用在次數已知
    #print(i)
    total += i
print("1到{}的總和為:{}".format(num, total))

#階乘，是所有小於等於該數的正整數的積，表示為n!
num = int(input("請輸入整數："))
total = 1
for i in range(1,num+1):
    #print(i)
    total *= i
print("{}的階乘為:{}".format(num, total))