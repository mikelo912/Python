# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:51:45 2023

@author: USER
"""

import os
print(os.getcwd()) #顯示目前所在的資料夾路徑
print('檔案lcc.txt是否存在?',os.path.exists('lcc.txt'))
print('資料夾good是否存在?',os.path.exists('good'))

print('lcc.txt是檔案嗎?',os.path.isfile('lcc.txt'))
print('good是檔案嗎?',os.path.isfile('good'))
print('good是目錄嗎?',os.path.isdir('good'))
for item in os.listdir('C:\\Users\\USER\\Desktop\\0509'): #印出資料夾內的東西
    print(item)
    
print(os.path.join('c:\\lcc','good','lcc.txt')) #拼接文件路徑
files = ['file1.txt', 'img1.jpg', 'hello.exe']
for f in files:
    name = os.path.join('c:\\lcc',f)
    print(name)