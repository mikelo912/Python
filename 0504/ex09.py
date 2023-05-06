# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:30:32 2023

@author: USER
"""

fn = "file02.txt"
with open(fn,encoding='utf-8') as f:
    data = f.read()
    newdata = data.replace('單身受薪','蔡依林') #用後面的字串取代前面的字串
    print(newdata.strip())
    
with open("news.txt",'w',encoding='UTF-8') as f:
    f.write(newdata.strip())
    
