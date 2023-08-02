# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 01:10:04 2023

@author: s9571
"""

import requests

URL = 'https://member.lccnet.com.tw/%E5%AD%B8%E7%BF%92%E8%A9%95%E5%83%B9Partial?key=0919951975&t=quk%2Fkk52bXNH2g3jj9TykT1NyA7Dr5Pv'

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

data = requests.get(URL,headers=header).text
print(data)