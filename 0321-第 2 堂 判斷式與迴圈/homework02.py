# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:00:09 2023

@author: USER
"""

#作業2
for i in range(1,10,2):
    for y in range(1,i+1):
        print(1,end="")
    print()
    
for i in range(1,10,2):
    msg = ""
    for a in range(i):
        msg +="1"
    print("{:^9}".format(msg)) #^表示置中對齊，9表示預留9個字元