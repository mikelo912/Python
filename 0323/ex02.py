# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:47:41 2023

@author: USER
"""

scores = [100,96,98,80,100]
items = [99,"一中",3.14,True]

print(items[1])
print(scores[0])

number = [1,2,3,4,5,6,7,8,9,0]

print(number[-1])
print(number[-2])
print(number[2:5])
print(number[ :5])
print(number[5: ])
print(number[1:9:2]) #間隔2
print(number[-1::-1])

for i in range(len(number)):
    print(number[i])
print()

for it in number:
    print(it)
