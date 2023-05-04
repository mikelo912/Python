# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:07:00 2023

@author: USER
"""

from datetime import datetime
import sys
import traceback

data = ['Python', 'Java', '聯成電腦']

def writeLog(errMsg):
    now = datetime.now()
    fileName = now.strftime('%Y%m%d') + ".log"
    happen = now.strftime('%H:%M:%S')
    with open(fileName,'a',encoding='utf-8') as fObj:
        fObj.write(happen + "" + errMsg + '\n')

try:
    print(data[0])
    print(data[5])
    
except Exception as ex: #例外處理

    msg = ex.args[0]
    cl, exc, tb = sys.exc_info()
    #紀錄最新一筆出錯的訊息
    lastCallStack = traceback.extract_tb(tb)[-1]
    
    fileName = lastCallStack[0] #取得發生的檔案名
    linenum = lastCallStack[1] #哪一行出問題
    fucName = lastCallStack[2] #哪一方法出問題
    
    error = "File:{}, line{}, detail:{}".format(fileName, linenum, msg)
    writeLog(error)
    
    #writeLog(ex.args[0])