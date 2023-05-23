# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import db
import json
import requests #上網用

url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=2000"
data = requests.get(url).text #抓取網址內的字串
bike = json.loads(data) #將json格式的資料，轉成字典型態
#print(bike)

for item in bike:
    station = item['sna']
    sql = "select * from ntpbike where station='{}'".format(station) #在資料表ntpbike內獲取station的所有資料
    #sql = "select * from ntpbike limit 10"
    db.cur.execute(sql) #執行資料庫物件
    
    #第一種寫法
    row = db.cur.fetchone()
    
    if row is None:
        #print("找不到")
        sql = "insert into ntpbike(station, tot, rent, space, area, address, lat, lng) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(item['sna'],item['tot'],item['sbi'],item['bemp'],item['sarea'],item['ar'],item['lat'],item['lng'])
        db.cur.execute(sql)
        db.conn.commit()
    else:
        #依station更新rent, space的值
        sql = "update ntpbike set rent='{}',space='{}' where station='{}'".format(item['sbi'],item['bemp'],item['sna'])
        db.cur.execute(sql)
        db.conn.commit()
db.conn.close()
        
    #count = db.cur.rowcount() #第二種寫法，計算筆數有多少
