# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:58:57 2023

@author: USER
"""

score = {'David':99,'Tom':89}
score['Bill'] = 90
score.setdefault('Peter')
print("分數:",score)
score['Peter'] = 61
score.update({'Mary':91})
print("分數:",score)

print('依姓名排序')
for key in sorted(score):
    print("%-10s %d"%(key,score[key]))

score.pop("Bill")
print()

for key in sorted(score,reverse=True):
    print("%-10s %d"%(key,score[key]))
    
print("字典清除:",score.clear())
score.update(David=87,John=66)
print(score)