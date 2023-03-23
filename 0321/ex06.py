# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:09:00 2023

@author: USER
"""

for a in range(2,10):
    for b in range(1,10):
        print(a,"*",b,"=",a*b,sep="",end="\t")
    print()

#作業1
for a in range(1,10):
    for b in range(2,10):
        print(b,"*",a,"=",b*a,sep="",end="\t")
    print()