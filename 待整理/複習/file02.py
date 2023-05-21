# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:09:38 2023

@author: thewh
"""

fn = "file02.txt"
msg = "Python 是一個超好學的程式語言"
data = ['聯成', '電腦', 'Python']
with open(fn,'w',encoding='utf-8') as f: #參數w為寫入，會覆蓋檔案內容
    f.write(msg + '\n')

    for line in data: #將data串列的內容一行一行寫入檔案
        f.write(line + '\n')