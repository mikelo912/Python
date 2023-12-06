# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:59:03 2023

@author: USER
"""

import mysql.connector

conn = mysql.connector.connect(host='mikelo912.mysql.pythonanywhere-services.com',user='mikelo912',passwd='Nana0121',database='myweb',auth_plugin='mysql_native_password',buffered=True)

cur = conn.cursor() #　dataset
