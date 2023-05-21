# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:40:19 2023

@author: thewh
"""

rows = 3
cols = 4

two_dimensional_list = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j)
    two_dimensional_list.append(row)

print(two_dimensional_list)