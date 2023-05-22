# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:55:15 2023

@author: USER
"""

import random #遷入radrom函式庫
print(random.random())

ans = random.randint(1,100) #由系統隨機取出1~100之間的一個數字
guess = 0

while guess != ans:
    print("輸入1~100之間猜數字：",end="")
    guess = int(input())
    if guess > ans:
        print("猜小一點")
    elif guess < ans:
        print("猜大一點")
print("猜對了")