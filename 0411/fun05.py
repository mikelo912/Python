# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:17:54 2023

@author: thewh
"""

#預設值引數
#函式中若有預設值引數時，你的位置引數必須在預設值引數之前，不可以在後
def name(sex,name,school='聯成',age=19): #預設值引數要擺在最後
    print("性別:", sex)
    print("姓名:", name)
    print("學校:", school)
    print(age)
    
name('Bill', '男')
name('Mary','女','台中女中')
name('Mary','女','台中女中',16)
name('Peter','男',age=14) #預設值引數，關鍵字引數可以混用