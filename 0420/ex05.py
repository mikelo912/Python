# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:53:12 2023

@author: USER
"""

def divResult(num1,num2):
    try:
        result = num1 // num2
        print('結果:',result)
    except Exception as e:
        print(e)
    finally: #有沒有錯誤都會執行
        print('計算完畢')
        
divResult(100, 20)
print()
divResult(100, 0)