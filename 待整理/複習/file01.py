# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:50:45 2023

@author: thewh
"""

print('第一種讀取檔案的方式')
fn = "file01.txt"
fobj = open(fn, encoding='utf-8') #開啟檔案，字元編碼為utf-8
data = fobj.read() #將檔案內容讀取至data
fobj.close() #關閉檔案
print(data)

print('第二種讀取檔案的方式')
with open(fn, encoding='utf-8') as file01:
#with語句執行完畢時，會自動關閉檔案
    for line in file01: #以行數來執行迴圈
        print(line)
        print('-'*30)