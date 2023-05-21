# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:24:43 2023

@author: thewh
"""

import sqlite3

conn = sqlite3.connect('demo.db')
name = input('輸入姓名:')
age = int(input('輸入年齡:'))
sex = input('輸入性別(Male/Female):')
birth = input('生日(yyyy-mm-dd):')

#增加一筆資料到表格
sql = "insert into students(sex,birthday,age,name) values('{}','{}',{},'{}')".format(sex,birth,age,name)

conn.execute(sql) #執行資料庫
conn.commit() #立即生效
conn.close() #關閉資料庫