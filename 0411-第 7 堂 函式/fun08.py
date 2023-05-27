# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:50:54 2023

@author: thewh
"""

def hot():
    print("很熱")

def cold(temp):
    print("現在溫度:",temp)
    
print(__name__) #印出主程式名稱

if __name__ == '__main__': #是主程式才會印出來
    print('Ya')