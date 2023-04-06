# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:42:40 2023

@author: USER
"""

member = {"Mary":30000,"Bill":1000000,"David":0}
keys = member.keys()
values = member.values()
print(keys)
print(values)

items = member.items()
print(items)

listv = list(values)
listk = list(keys)
listi = list(items)

print("最小值:",min(listv))
print("最大值:",max(listv))

for it in listi:
    print(it)
    print(it[0],it[1])
print()

for k,v in listi:
    print(k,v)