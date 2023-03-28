# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:35:49 2023

@author: USER
"""

a = int(input("請輸入第一個數字:"))
b = int(input("請輸入第二個數字:"))
c = int(input("請輸入第三個數字:"))

if a+b > c and b+c > a and c+a >b:
    print("這三個數字可以構成三角形")
else:
    print("這三個數字不能構成三角形")
    
if a == b and a !=c:
    print("此三角形為等腰三角形")
elif b == c and b !=a:
    print("此三角形為等腰三角形")
elif a == c and a !=b:
    print("此三角形為等腰三角形")
elif a == b and a == c:
    print("此三角形為正三角形")   
    
a = int(input("請輸入第一個數字:"))
b = int(input("請輸入第二個數字:"))
c = int(input("請輸入第三個數字:"))

if a+b > c and b+c > a and c+a >b:
    print("這三個數字可以構成三角形")
    if a == b == c:
        print("此三角形為正三角形")
    elif a == b or a == c or b == c:
        print("此三角形為等腰三角形")
    
else:
    print("這三個數字不能構成三角形")
