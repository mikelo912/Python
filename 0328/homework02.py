# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:11:24 2023

@author: USER
"""

'''
作業2
由使用者分別輸入六個數字，並放入串列中
請用巢狀迴圈進行由大至小排序，並印出結果
'''

number = list()

while len(number) < 6:
    num = int(input("請輸入六個數字:"))
    if number.count(num) == 0:
        number.append(num)
    else:
        print(num,"重複")
print(number)

leng = len(number)
for i in range(leng-1):
    for x in range(leng-i-1):
        if number[x] < number[x+1]:
            number[x],number[x+1] = number[x+1],number[x]
            '''
            temp = number[x]
            number[x] = number[x+1]
            number[x+1] = temp
            '''
print(number)