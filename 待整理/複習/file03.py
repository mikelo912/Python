# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:20:52 2023

@author: thewh
"""
#使用try-except處理異常

from datetime import datetime
import sys
import traceback #獲取異常的詳細訊息

data = ['Python', 'Java', '聯成電腦']

def writeLog(errMsg):
    now = datetime.now() #將目前時間寫入now
    fileName = now.strftime('%Y%m%d') + ".log" 
    '''
    strftime()將時間格式化為字串
    %Y代表四位數的年份、%y代表兩位數的年份、%m代表幾月、%d代表幾日
    %H代表幾點、%M代表幾分、%S代表幾秒
    '''
    happen = now.strftime('%H:%M:%S')
    with open(fileName,'a',encoding='utf-8') as fObj:
        fObj.write(happen + " " + errMsg + '\n')

try:
    print(data[0])
    print(data[5]) #此行會發生異常
    
except Exception as ex: #例外處理

    msg = ex.args[0] 
    '''
    例外的第一個參數，args用於傳遞任意數量的位置參數，會將這些參數打包成元組
    '''
    exc_type, exc_obj, exc_tb = sys.exc_info()
    #print(exc_type)
    #print(exc_obj)
    #print(exc_tb)
    '''
    sys.exc_info() 方法返回一個元組，其中包含三個值：
    異常類型、異常的實例和異常的追蹤訊息。
    這三個值分別被賦值給變數exc_type, exc_obj, exc_tb
    '''
    lastCallStack = traceback.extract_tb(exc_tb)[-1] #紀錄最新一筆出錯的訊息
    
    fileName = lastCallStack[0] #取得發生的檔案名
    linenum = lastCallStack[1] #哪一行出問題
    funName = lastCallStack[2] #哪一方法出問題
    
    error = "File:{}, Line:{}, Function:{}, Detail:{}".format(fileName, linenum, funName, msg)
    writeLog(error)
    
    #writeLog(ex.args[0])