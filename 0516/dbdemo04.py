# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:07:34 2023

@author: thewh
"""

import sqlite3
conn = sqlite3.connect('demo.db')
sql = "select * from students"
sql = "select * from students where sex='F'"
sql = "select * from students where sex='F' and age <= 25"
sql = "select * from students where sex='F' and age >= 20 and age <= 25"
cur = conn.cursor() #資料集物件
cur.execute(sql)
res = cur.fetchall()

for row in res:
    print('編號:',row[0])
    print('姓名:',row[1])
    print('年齡:',row[2])
    print() 

conn.close()