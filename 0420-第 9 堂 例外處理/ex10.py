# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:10:29 2023

@author: USER
"""

def score(number):
    if number <0:
        return '不可小於0'
    else:
        assert number >=0, '輸入值要大於0'
        print('分數:',number)
    
score(60)