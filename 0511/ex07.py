# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:23:56 2023

@author: USER
"""

import openpyxl
from openpyxl.chart import BarChart,Reference

wb = openpyxl.Workbook()
ws = wb.active

sales = [
        ['區域','2021年','2022年'],
        ['台北',31000,29100],
        ['台中',49980,31000],
        ['台南',35970,45655]
        ]
#數字才可以建立圖表

for row in sales:
    ws.append(row)
    
chart = BarChart()
chart.title = '各區銷售額'
chart.x_axis.title = '地區' #X軸代表的東西
chart.y_axis.title = '金額'

data = Reference(ws,min_col=2,max_col=3,min_row=1,max_row=4) #填入圖表資料
chart.add_data(data, titles_from_data=True)

xtitle = Reference(ws,min_col=1,min_row=2,max_row=4) #定義X軸，標示出區域
chart.set_categories(xtitle)
ws.add_chart(chart,'F1') #圖表要放在哪個儲存格

wb.save('sales.xlsx')