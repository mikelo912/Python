# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:56:52 2023

@author: s9571
"""

#題目：輸入三個整數x,y,z，請把這三個數由小到大輸出。

number = list()

while len(number) <3:
    x = int(input('請輸入三個整數:'))
    if number.count(x) == 0:
        number.append(x)
    else:
        print('數字重複，請輸入其他整數')



leng = len(number)
for i in range(leng-1): 
    for j in range(leng-i-1): #比較次數隨著i值遞減
        #如果前面數字大於後面數字，直接將兩者對調
        if number[j] > number[j+1]:
            number[j+1],number[j] = number[j],number[j+1]
            
print(number)