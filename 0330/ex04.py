# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:45:01 2023

@author: USER
"""

students = {"Tom":98,"David":70,"Mary":100}
print(students["David"])
#print(students["Bill"]) #沒有key無法取值

fruit = dict(a = "Apple", b = "Banana")
print(fruit["b"])

number = dict() #{}
number[1] = "台中一中"
number[10] = "台中女中"
print(number)
print(number[10])

print(students.get('Bill'))
print(students.get('Bill','沒有key'))