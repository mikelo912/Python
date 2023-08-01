# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import json

url = "https://tw.buy.yahoo.com/search/product?p=switch"

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
data = requests.get(url,headers=header).text    
#print(data)

soup = BeautifulSoup(data,'html.parser')

goods = soup.find_all('a',class_='sc-1drl28c-1 hcbDur')

allimgs = soup.find(id="isoredux-data").get("data-state")
images = json.loads(allimgs)
product_img = images['search']['ecsearch']['hits']
#print(product_img)


for item in goods:
    
    link = item.get('href')    
    title = item.find('img').get('alt')
    
    allprice = item.find('div',class_='sc-1ap2njs-0 dPpkAj')
    
    price = allprice.find_all('span',class_='eCzBYn')
    
    #for pr in price:
    #    print(pr.text)
    
    #print('特價：',price[0].text)
    intprice = price[0].text.replace('$','')
    intprice = intprice.replace(',','')
    
        
    for row in product_img:
        pPhoto = ""
        if link == row['ec_item_url']:
            pPhoto = row['ec_image']
            break
    
    
    print(title)
    if len(price) == 2:
        print('原價：',price[1].text)
    print('特價：',intprice)
    print(link)
    print('商品圖片:',pPhoto)
    print()