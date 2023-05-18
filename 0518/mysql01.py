# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:31:32 2023

@author: USER
"""

import db

name = input('輸入姓名:')
age = int(input('輸入年齡:'))
sex = input('輸入性別(F/M):')
birth = input('生日(yyyy-mm-dd):')

#增加一筆資料到表格
sql = "insert into students(sex,birthday,age,name) values('{}','{}',{},'{}')".format(sex,birth,age,name)

db.cur.execute(sql) #執行資料庫
db.conn.commit() #立即生效
db.conn.close() #關閉資料庫