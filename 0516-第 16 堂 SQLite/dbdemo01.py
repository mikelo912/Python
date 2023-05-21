# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:56:24 2023

@author: thewh
"""

import sqlite3

conn = sqlite3.connect('demo.db') #建立一個SQLite的連線，db為database的縮寫

#if not exists不存在就會建立資料庫
#integer整數型態，裡面是主key，會自動遞增
#欄位名稱有name,age,sex,birthday
#varchar(30)是字串，30為長度
sql = "create table if not exists students(id integer primary key autoincrement, name varchar(30), age int, sex varchar(2), birthday char(10))"

conn.execute(sql) #執行資料庫
conn.commit() #立即生效
conn.close() #關閉資料庫