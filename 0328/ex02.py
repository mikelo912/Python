# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:44:59 2023

@author: USER
"""

students = ['Bill', 'Mary', 'David', 'Peter']
students.remove('David')
print(students)

if students.count('Tom') > 0:
    students.remove('Tom')

print()
number = [1,2,3,4,5,6,7,8]
n = number.pop() #由後往前抓
print(n)
n = number.pop(5) #抓索引值內的值
print(n)
print(number)