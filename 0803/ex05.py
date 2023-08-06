# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:58:08 2023

@author: USER
"""

import re
from bs4 import BeautifulSoup

html = """
<div class="content">
E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
<ul class="price">定價：360 元 </ul>
<img src="http://test.com.tw/p1.jpg">
<img src="http://test.com.tw/p2.jpg">
<img src="http://test.com.tw/p3.png">
</div>
"""

soup = BeautifulSoup(html,'html.parser')
data = soup.select('.price')[0].text #select是css選擇器，在css當中class名稱前面要加.
print(data)

#第一種寫法
# pattern = '[0-9]+'
# data = re.search(pattern, data)
# print(data.group())

#第二種寫法
result = re.findall('[0-9]+', data)
print(result[0])

# .的意義是符合除「\r」「\n」之外的任何單個字元 
# 字元\ => 將下一個字元標記為一個特殊字元
emails = re.findall(r"[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+",html)
for email in emails:
    print(email)