# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re #正則表示式

text = "https://www.lccnet.com.tw"
text2 = "python聯成電腦python"

print(re.search('https',text).span()) #搜尋https在text中的起點和終點，以索引值表示
print(re.search('lccnet',text).span())
print(re.search('python',text2).span()) #只會抓第一個字
#print(re.search('Python',text2).span()) #找不到會出現錯誤
print(re.search('Python',text2,flags=re.I).span()) #忽略大小寫
print(re.search('python',text2).group()) #抓出匹配的字