# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 09:59:39 2023

@author: thewh
"""

#函式的權限是最高的

def sayHello(): #無參數的函式
    print("hello")
    print("你好")
    print("Bon ju")

sayHello()
print()

start = 99 #全域變數

def runfor(start,end,sep): #有參數的函式
    #在函式中，所定義的變數名稱，都是區域變數(除非有特別指定)
    a = 10
    for i in range(start,end,sep): #參數名稱要一樣
        print(i)
        
runfor(5,15,3) #位置參數
print()
print(start)