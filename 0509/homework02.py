# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

I = input('請輸入當月利潤:')

if I <= 100000:
    bonus = I*0.1
elif I > 100000 and I <= 200000:
    bonus = 100000*0.1 + (I-100000)*0.075
elif I > 200000 and I <= 400000:
    bonus = (I-200000)*0.05
elif I > 400000 and I <= 600000:
    bonus = (I-400000)*0.03
    