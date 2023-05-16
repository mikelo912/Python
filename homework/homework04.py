# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:31:55 2023

@author: thewh
"""

print('題目：輸入某年某月某日，判斷這一天是這一年的第幾天？')

year = int(input('請輸入年份:'))
month = int(input('請輸入月份:'))
day = int(input('請輸入日期:'))

#當月份的天數用day表示，故月份-1
#month -= 1

days = 0
for i in range(month):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10:
        days += 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        days += 30
    elif i == 2 and year % 4 == 0:
        days += 29
    elif i == 2 and year % 4 != 0:
        days += 28
    
ans = days + day #上個月之前的天數加上當月日期 

print('%4d/%2d/%2d是%4d的第%3d天'%(year,month,day,year,ans))