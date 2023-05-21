# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:07:34 2023

@author: thewh
"""

import sqlite3
conn = sqlite3.connect('demo.db')
#sql = "select * from students"
#where子句:僅獲取滿足指定條件的資料
sql = "select * from students where sex='F'"
#sql = "select * from students where sex='F' and age <= 25"
#sql = "select * from students where sex='F' and age >= 20 and age <= 25"
cur = conn.cursor() #資料集物件
cur.execute(sql)
res = cur.fetchall() #檢索某個查詢的所有欄，此方法返回一個元組

for row in res:
    print('編號:',row[0])
    print('姓名:',row[1])
    print('年齡:',row[2])
    print('性別:',row[3])
    print() 

conn.close()