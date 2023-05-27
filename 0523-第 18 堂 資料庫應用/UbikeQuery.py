# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:21:27 2023

@author: USER
"""

import db

print('Ubike查詢')
while True:
    num = input('查詢站名請輸入1,地區查詢請輸入2,地址查詢請輸入3, 離開請輸入q:')
    if num == 'q':
        break
    if num == '1':
        station = input('請輸入站名:')
        sql = "select * from ntpbike where station like '%{}%'".format(station)
    elif num == '2':
        sql = "select distinct area from ntpbike" #distinct 略過重複項
        db.cur.execute(sql)
        data = db.cur.fetchall()
        for row in data:
            print(row[0],end=',')
        print()
        area = input('請輸入地區:')
        sql = "select * from ntpbike where area='{}'".format(area)
                
    db.cur.execute(sql)
    data = db.cur.fetchall()
    for row in data:
        print(row[1],'可租:',row[3],'可還:',row[4])
db.conn.close()