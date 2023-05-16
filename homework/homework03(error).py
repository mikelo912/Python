# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:27:21 2023

@author: s9571
"""

print('題目：一個整數，它加上100後是一個完全平方數，再加上168又是一個完全平方數，請問該數是多少？')

square1 = []
square2 = []

#100是10的平方，故從10開始找
for i in range(10,20):
    square1.append(i*i-100)

for j in range(10,20):
    if j*j-168 < 0:
        continue
    else:
        square2.append(j*j-168)

for k in range(len(square1)):
    ans = []
    
    for l in square1:
        if l in square2:
            ans.append(l)


print('該數為',ans)