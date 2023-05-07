# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:37:54 2023

@author: thewh
"""

'''
作業:大樂透對獎
1.電腦開出1-49之間6個號碼(不可重複)
2.使用者可下注?注，由使用者輸入
  1-49，6個號碼不重複
3.對獎 顯示中了多少注(二個號碼即中獎)
'''

import random #帶入亂數函式庫
#print(random.random()) #產生亂數，變數名需和函式名一樣，原始型態為浮點數
number = []
for i in range(1,50,1):
    number.append(i)
#print(random.choice(number)) #從ans序列隨機挑選一個值
    




'''
做出一個迴圈(跑?次)
印出一組六個號碼(要產生六個序列)
'''

lotto = eval(input("請輸入要下多少注:"))
for i in range(lotto):
    a = []
    num = number
    for j in range(6):
        a.append(random.choice(number))
        number.remove(a[j])
    print(a)
#超過9注會error，因串列number索引只到48

#產生隨機六個號碼(不重複)
#開獎號碼
lottery = []

for i in range(6):
    lottery.append(random.choice(number)) #產生隨機六個號碼
    number.remove(lottery[i])
print("開獎號碼:",lottery)

#對獎 顯示中了多少注(二個號碼即中獎)
'''
比較對獎號碼跟每一注號碼
確認是否有兩個以上相同的值
'''

from collections import Counter

combined_list = lottery + a
counts = Counter(combined_list)
common_elements = [element for element, count in counts.items() if count >= 2]

if common_elements:
    print("恭喜你中獎了!!")
else:
    print("真可惜，沒有中獎")