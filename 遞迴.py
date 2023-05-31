# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:43:56 2023

@author: s9571
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))