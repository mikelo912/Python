# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:48:40 2023

@author: USER
"""

import openpyxl #excel函式庫

file = 'school.xlsx'
wb = openpyxl.load_workbook(file, data_only=True) #data_only抓儲存格呈現的值
ws = wb['students']
print('所選工作表名稱:',ws.title)

for row in ws.rows:
    for cell in row: #cell是儲存格
        print(cell.value,end=' ')
    print()