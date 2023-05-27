# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:47:07 2023

@author: USER
"""

import openpyxl

wb = openpyxl.Workbook() #建立空白活頁簿
ws = wb.active

ws.title = 'member' #定義活頁簿名稱
wb.save('lcc.xlsx')