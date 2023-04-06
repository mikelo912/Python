# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:01:14 2023

@author: USER
"""

score = {'Tom':95,'Bill':78,'John':47,'Edward':67,'Eric':52,'Ivy':67,'David':35}
print("及格有\n",{k:v for k,v in score.items() if v >= 60}) #字典生成式
print("不及格有:\n",{k:v for k,v in score.items() if v < 60})

print()

minScore = min(zip(score.values(),score.keys()))
maxScore = max(zip(score.values(),score.keys()))

print("最高分:",maxScore)
print("最低分:",minScore)

d1 = [1,2,3]
d2 = [4,5,6]

maxD = zip(d1,d2)
print(list(maxD))