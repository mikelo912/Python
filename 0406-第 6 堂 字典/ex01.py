# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:14:30 2023

@author: USER
"""

student = {"David":99,"Peter":88,"Mary":100}
print("David" in student) #找值有沒有在裡面
print("Bill" in student)

while True:
    search = input("學生姓名q離開:")
    if search == 'q':
        break
    if search in student:
        print(search,"分數:",student[search])
    else:
        score = int(input("請輸入分數:"))
        student[search] = score

print(student)