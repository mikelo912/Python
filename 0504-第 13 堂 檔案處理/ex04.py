# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:34:44 2023

@author: USER
"""

fn = "file02.txt"

with open(fn, encoding='utf-8') as fObj:
    #data = fObj.read()
    for line in fObj:
        print(line)
        print('-'*30)
    
#print(data)