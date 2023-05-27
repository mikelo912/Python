# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:17:53 2023

@author: thewh
"""

money = 199
def interest(rate):
    global money #將money設為全域變數，裡面的變數會與外面同步
    money = 100000 #區域變數
    inter = money * rate
    print("利息:", inter,'元')
    
    return "已執行" #需要回傳值的時候加上return
    
interest(0.06)

print(money)
print()
print(interest(0.01))