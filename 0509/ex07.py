# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:41:55 2023

@author: USER
"""

import csv

fileName = 'mycsv2.csv'
allData = [['name','age','sex'],['Bill','18','M'],['Mary','21','F']]

with open(fileName,'w',encoding='utf-8',newline='') as fO:
    csvWriter = csv.writer(fO)
    
    for row in allData:
        csvWriter.writerow(row)