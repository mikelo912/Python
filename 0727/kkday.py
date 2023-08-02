# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 04:20:42 2023

@author: s9571
"""

import requests
import json

header = {

'authority':'www.kkday.com',
'method':'GET',
'path':'/zh-tw/area_api/ajax_get_recommend_top_products?areaCode=A01-001-00020',
'scheme':'https',
'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':
'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
'Content-Type':
'application/x-www-form-urlencoded;charset=UTF-8',
'Cookie':
'csrf_cookie_name=e575c25dfbcf2409db76fb3fa3381544; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%224a146f7b736e5c9718053fc52d4fc7a2%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1690993216%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5f816e190c329db61a676ac446cfc9b1; country_lang=zh-tw; currency=TWD; KKUD=4a146f7b736e5c9718053fc52d4fc7a2; _gcl_au=1.1.965510088.1690993237; _ga_RJJY5WQFKP=GS1.1.1690993236.1.1.1690993237.59.0.0; _ga=GA1.2.1411687130.1690993237; _gid=GA1.2.373278112.1690993237; _fbp=fb.1.1690993237218.538369492; _hjFirstSeen=1; _hjIncludedInSessionSample_628088=0; _hjSession_628088=eyJpZCI6IjY1OTZmMWQ4LWU2MDQtNGIwNS04MThkLWJlOGQwZDY1NTc3MiIsImNyZWF0ZWQiOjE2OTA5OTMyMzkwMjUsImluU2FtcGxlIjpmYWxzZX0=; rskxRunCookie=0; rCookie=lqklzod14ed2qeydunm41tlktxppti; CookieConsent={stamp:%27uD9NdBbDvJ3eDzWdM4TvRQaJfoEGvlcyNEOSZf/LO6+mpI3NG2HHZg==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1690993225129%2Cregion:%27tw%27}; _hjSessionUser_628088=eyJpZCI6IjE4MTJiOTkzLWViYTgtNTYzZC1hNGNlLTU5MjU5NjM4NGE0OCIsImNyZWF0ZWQiOjE2OTA5OTMyMzkwMTcsImV4aXN0aW5nIjp0cnVlfQ==; _dc_gtm_UA-49763723-1=1; _dc_gtm_UA-117438867-1=1; _dd_s=rum=0&expire=1690994262962; datadome=4Gr1FAxxajRNy66XeGiszYCbVgXeG_-Untok~sKm8~nascYf8nq6W3S23GW4nySxzDAS7FYNrzYwFYJGk9WkL~KUUTI2xaaSC6615dTjyD_bhJNhaYgZUcoji9H0mRp0; lastRskxRun=1690993363515',
'Dnt':'1',
'Referer':
'https://www.kkday.com/zh-tw/city/kinmen',
'Sec-Ch-Device-Memory':'8',
'Sec-Ch-Ua':
'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
'Sec-Ch-Ua-Arch':'"x86"',
'Sec-Ch-Ua-Full-Version-List':
'"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.110", "Chromium";v="115.0.5790.110"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Model':'""',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
'X-Requested-With':
'XMLHttpRequest'

}
    
url = 'https://www.kkday.com/zh-tw/area_api/ajax_get_recommend_top_products?areaCode=A01-001-00020'

data = requests.get(url,headers=header).text
#print(data)
travel = json.loads(data)
travel = travel['data']

for row in travel:
    title = row['name']
    info = row['introduction']
    photo = row['img_url']
    price = row['display_sale_price']
    print(title)
    print(info)
    print(photo)
    print('TWD',price)
    print()