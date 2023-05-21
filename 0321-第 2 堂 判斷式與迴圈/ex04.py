# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:46:02 2023

@author: USER
"""

i = 1
while i < 10: #滿足條件則執行
    print(i)
    i += 1
    
print("="*30)

num = int(input("輸入次數："))
for i in range(num,0,-1): #range(起始值,終止值,間隔值)
    print(i)