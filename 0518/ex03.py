# -*- coding: utf-8 -*-
"""
Created on Thu May 18 19:55:27 2023

@author: USER
"""

import sqlite3
conn = sqlite3.connect('demo.db')

try:
    while True:
        name = input('請輸入姓名,按q離開:')
        if name == 'q':
            break
        sql = "select * from students where name like '%{}%'".format(name)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        
        if data == None:
            print('找不到')
        else:
            for row in data:
                print('ID:',row[0])
                print('姓名:',row[1])
                print('年齡:',row[2])
                print('性別:',row[3])
        num = int(input('請輸入欲修改ID:'))
        age = int(input('請輸入欲修正的年齡:'))
        q = input('修改=>1, 刪除=>2, 不做任何異動=>n')
        if q == '1':
            sql = "update students set age={} where id={}".format(age, num)
            cur.execute(sql)
            conn.commit()
        elif q == '2':
            sql = "delete from students where id = {}".format(num)
            cur.execute(sql)
            conn.commit()
            
finally:        
    conn.close()