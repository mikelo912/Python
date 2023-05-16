# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 10:52:55 2023

@author: thewh
"""

print('題目：有四個數字：1、2、3、4，能組成多少個互不相同且無重複數字的三位數？各是多少？')

hundred = 100
ten = 10
one = 1
num = 0
ans = []

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i == j or j == k or k == i:
                break
            else:
                ans.append(one*i + ten*j + hundred*k)
                ans.append(one*j + ten*k + hundred*i)
                ans.append(one*k + ten*i + hundred*j)
                num += 3

print('可以組成',num,'種')
print(ans)
