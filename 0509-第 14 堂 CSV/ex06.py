# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:19:35 2023

@author: USER
"""

import csv
fileName = 'mycsv.csv'
with open(fileName,'w',encoding='utf-8',newline='') as fO:
    csvWriter = csv.writer(fO)
    csvWriter.writerow(['name','age','sex'])
    csvWriter.writerow(['Bill','18','M'])
    csvWriter.writerow(['Mary','21','F'])