# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:41:49 2023

@author: USER
"""

import db

try:
    while True:
        name = input('請輸入姓名,按q離開:')
        if name == 'q':
            break
        sql = "select * from students where name like '%{}%'".format(name)
        db.cur.execute(sql)
        data = db.cur.fetchall()
        if data == None:
            print('找不到')
        else:
            for row in data:
                print('姓名:',row[1])
                print('年齡:',row[2])
                print('性別:',row[3])
            
finally:        
    db.conn.close()