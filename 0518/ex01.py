# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3
conn = sqlite3.connect('demo.db')

try:
    while True:
        name = input('請輸入姓名,按q離開:')
        if name == 'q':
            break
        sql = "select * from students where name ='{}'".format(name)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()
        if data == None:
            print('找不到')
        else:
            print('姓名:',data[1])
            print('年齡:',data[2])
            print('性別:',data[3])
            
finally:        
    conn.close()