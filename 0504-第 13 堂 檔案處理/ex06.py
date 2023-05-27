# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:47:05 2023

@author: USER
"""

fn = "file03.txt"
msg = "Python 是一個超好學的程式語言"
data = ['聯成', '電腦', 'Python']
with open(fn,'w',encoding='utf-8') as f: #參數w為寫入，會覆蓋檔案內容
    f.write(msg + '\n')

    for line in data:
        f.write(line + '\n')
