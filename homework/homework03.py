# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:27:21 2023

@author: s9571
"""

print('題目：一個整數，它加上100後是一個完全平方數，再加上168又是一個完全平方數，請問該數是多少？')
ans = 1

while bool(ans): 
    x = 1
    y = 1
    m = 1
    n = []
        
    m*m == x + 100
    n*n == y + 100 + 168
    
    for m in range(169):
        if (m+n)*(m-n) == 168:
            print(m,n)
        else:
            continue
        
print(bool(ans))