# -*- coding: utf-8 -*-
"""
Created on Thu May 18 19:38:39 2023

@author: USER
"""

import sqlite3
conn = sqlite3.connect('demo.db')

try:
    while True:
        name = input('請輸入姓名,按q離開:')
        if name == 'q':
            break
        #查詢名字內"包含使用者輸入字母"的資料
        #ex: 如果是'M%',可以查詢到名字以’M‘字母開頭的資料
        sql = "select * from students where name like '%{}%'".format(name)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        if data == None:
            print('找不到')
        else:
            for row in data:
                print('姓名:',row[1])
                print('年齡:',row[2])
                print('性別:',row[3])
            
finally:        
    conn.close()