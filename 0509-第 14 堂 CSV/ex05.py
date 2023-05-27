# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:15:01 2023

@author: USER
"""

import csv
fileName = 'YouBike.csv'
with open(fileName, encoding='utf-8') as fO:
    csvdict = csv.DictReader(fO) #DictReader()將每行資料映射到字典
    for row in csvdict:
        #print(row)
        print(row['sna'])
        print(row['ar'])
        print()
        