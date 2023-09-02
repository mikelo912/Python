# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:25:42 2023

@author: s9571
"""

import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',user='root',passwd='Nana0121',database='myweb',auth_plugin='mysql_native_password')
cur = conn.cursor()