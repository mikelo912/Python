# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:24:48 2023

@author: USER
"""

import random

numbers = list()
n = int(input('請輸入要下多少注:'))

for i in range(n):
    num = list()
    while len(num) < 6:
        ran = random.randint(1,49)
        if num.count(ran) == 0:
            num.append(ran)
    numbers.append(num)
print(numbers)

#開獎
result = list()
while len(result) < 6:
    ran = random.randint(1,49)
    if result.count(ran) == 0:
        result.append(ran)
print('開獎號碼:',result)

print('開始兌獎')
for row in numbers:
    point = 0
    for n in row:
        if result.count(n) == 1:
            point += 1
    if point >= 2:
        print(row,'中了',point,'個號碼，恭喜中獎')
    else:
        print(row,'中了',point,'個號碼，銘謝惠顧')