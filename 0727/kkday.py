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
'csrf_cookie_name=0702cbca8ecbd4d7ea119bd79c387ab9; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%228d5cc7f61c7fd58f96a26344b7b84b30%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1690835895%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D095fe002f42287d227030d0c3b618650; country_lang=zh-tw; currency=TWD; KKUD=8d5cc7f61c7fd58f96a26344b7b84b30; _gcl_au=1.1.611843015.1690835913; _gid=GA1.2.476457605.1690835915; _fbp=fb.1.1690835915801.1197242517; _hjFirstSeen=1; _hjIncludedInSessionSample_628088=0; _hjSession_628088=eyJpZCI6Ijc3Mjg4ZDg0LWQzMDAtNDM3OC1iMTQ1LTRjZjg3NDUzMWU1MyIsImNyZWF0ZWQiOjE2OTA4MzU5MTU4NDUsImluU2FtcGxlIjpmYWxzZX0=; rskxRunCookie=0; rCookie=4obe1d4uavuxwnvrtlhgdlkrc1riw; _ga_RJJY5WQFKP=GS1.1.1690835913.1.1.1690835924.49.0.0; _ga=GA1.2.2126823123.1690835913; _hjSessionUser_628088=eyJpZCI6IjQxNzdkNzdmLTY1ZTItNTQyMS1iNWQzLWQwMjY4ZGY1NjM5YiIsImNyZWF0ZWQiOjE2OTA4MzU5MTU4MzIsImV4aXN0aW5nIjp0cnVlfQ==; lastRskxRun=1690835926370; CookieConsent={stamp:%27BSS6vJTwzlKZxxDh0ZSaZPlLQexTIlxf3SNAd8YSL4xn8mebMMcYBw==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1690835928142%2Cregion:%27tw%27}; datadome=Yspb-1CEdGvqAas9KNF6LUzgg4LG6gfmeJGi30~mSBDVhH9Svlaxs4e_JoGTJK7qGVGKuaztA8J1MKRIJowwYXk2Ac6eYrVi8tQCpMZVcHIChbHcVjxKK7rIVkEXTQ5; _dd_s=rum=2&id=070bbaed-f16b-4d7e-b4ef-9913c95c5b89&created=1690835912388&expire=1690837054009',
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
print(data)