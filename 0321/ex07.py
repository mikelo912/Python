# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:30:59 2023

@author: USER
"""

for i in range(1,6):
    for y in range(1,i):
        print(y,end="")
    print()

for i in range(1,6):
    for y in range(1,i+1):
        print(i,end="")
    print()
    
#作業2
for i in range(1,10,2):
    for y in range(1,i+1):
        print(1,end="")
    print()
    
#作業3
for i in range(5,0,-1):
    for y in range(i,0,-1):
        print(i,end="")
    print()
if i==1:
    for i in range(2,6):
        for y in range(1,i+1):
            print(i,end="")
        print()