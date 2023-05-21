# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:07:34 2023

@author: thewh
"""

import sqlite3
conn = sqlite3.connect('demo.db')
sql = "select * from students" #選擇所有列
result = conn.execute(sql)


for row in result:
    print('姓名:',row[1])
    print('性別:',row[3])
    print('生日:',row[4])
    print()
    
conn.commit()
conn.close()