# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:03:16 2023

@author: USER
"""

fn = "file04.txt"
msg = "Python 是一個超好學的程式語言"
data = ['聯成', '電腦', 'Python']
with open(fn,'a',encoding='utf-8') as f: #繼續寫入檔案
    f.write(msg + '\n')

    for line in data:
        f.write(line + '\n')