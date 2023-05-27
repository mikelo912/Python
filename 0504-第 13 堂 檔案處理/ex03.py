# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:09:20 2023

@author: USER
"""

fn = "file01.txt"
fobj = open(fn) #開啟檔案
data = fobj.read() #讀取內容
fobj.close()
print(data)

fn = "file02.txt"
fobj = open(fn,encoding='utf-8') #開啟檔案
data = fobj.read() #讀取內容
fobj.close()
print(data)