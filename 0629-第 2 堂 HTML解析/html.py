# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:53:41 2023

@author: s9571
"""

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
<img src="iu.jpg">

<div id="area">
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
<img src="iu.jpg">
</div>

</body></html>
"""
soup = BeautifulSoup(html_doc,'html.parser') #parser的中文是解析器
#print(soup.prettify())

title = soup.find('title') #抓標籤及內容，只抓第一個
h2 = soup.find('h2').text #抓內容文字
p = soup.find_all('p') #抓全部標籤及內容
"""
print(title)
print(h2)
print(p)
print(title.text) #抓內容文字
"""
a = soup.find('a')
print(a)
a_id = soup.find(id='link2')
print(a_id)

link = a.get('href') #get抓標籤裡面的屬性
print(link) #顯示超連結網址
print(a.text) #顯示超連結的文字
img = soup.find('img').get('src')
print(img) #抓圖片網址

textarea = soup.find(id="area")
print(textarea)

tp = textarea.find('p').text
print(tp)