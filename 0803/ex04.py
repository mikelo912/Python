# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:07:41 2023

@author: USER
"""

import re
# *的意義是前一字元或括號內出現零次或多次
# a*b* => aaaaab 符合, aabb 符合, ab符合, bbb符合
# +的意義是前一字元或括號內出現"一次"或多次
# 可用","或" "分隔單字
text = "find abbbbc, bc, skip c, bbbbcc"
pattern = "a*b+c"
result = re.findall(pattern,text)
print(result)

text2 = "good 123 ya 456 lccnet 789"
result = re.findall('([a-z]+)',text2)
print(result)

text3 = "Year 2023 Month 08 Day 03"
pattern = "[0-9]+"
result = re.findall(pattern,text3)
print(result)

pattern = "[A-Za-z]+" #[]內可以存在多種規則
result = re.findall(pattern,text3)
print(result)

pattern = "a*b*c"
result = re.findall(pattern,text)
print(result) #c出現了5次，所以會有串列內5筆資料