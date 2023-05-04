# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range(20):
    if i == 10:
        break #離開當前迴圈
    if i%4 == 0:
        continue #放棄一次，下面皆不執行
    if i == 3:
        pass #跳過程式碼，開發者需再回來撰寫程式，目前先放著不處理
    print(i)