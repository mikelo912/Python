# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

filename = "dictcsv.csv"

with open(filename,'w',encoding='utf-8',newline='') as f:
    fields = ['name','sex','age'] #定義第一欄位有哪些
    #建立Writer的物件
    dictWriter = csv.DictWriter(f, fieldnames=fields) 
    #寫入標題
    dictWriter.writeheader()
    dictWriter.writerow({'name':'陳美麗','sex':'女','age':'30'})
    dictWriter.writerow({'name':'陳聰明','sex':'男','age':'21'})