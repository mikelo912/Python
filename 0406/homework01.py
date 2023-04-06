# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input("幾層?"))
data = [1]
for i in range(n):
    print(data)
    plist = []
    plist.append(data[0])
    for i in range(len(data)-1):
        plist.append(data[i]+data[i+1])
    plist.append(data[-1])
    data = plist