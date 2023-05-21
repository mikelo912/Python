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
ans = []
for i in range(1,50,1):
    ans.append(i)
print(random.choice(ans)) #從ans序列隨機挑選一個值

#產生隨機六個號碼
a = []
for i in range(6):
    a.append(random.choice(ans))
print(a)


lotto = input("請輸入要下多少注，按q離開")
while True:
    if lotto == 'q':
        break
    
