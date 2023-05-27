# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:31:20 2023

@author: USER
"""

number = [99,66,33,45,65,89,80]
number.sort() #小到大
print(number)

number.sort(reverse=True) #大至小
print(number)

number = [99,66,33,45,65,89,80]
newNum = sorted(number)
print(newNum)
print(number)
newNum2 = sorted(number,reverse=True)
print(newNum2)
print(number)
