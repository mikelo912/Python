# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

answer = input("請輸入\"快樂\"的英文:")
while answer.upper() != "HAPPY": #upper()可以將字串變為大寫
    answer = input("答錯了，請重新輸入\"快樂\"的英文:")
else:
    print("答對了!")