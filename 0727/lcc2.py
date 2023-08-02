# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 01:29:24 2023

@author: s9571
"""

import requests

url = "https://member.lccnet.com.tw/signout/LearningRecord.aspx"
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
param = {
    '關鍵字':'0919951975',
    '授課堂數':'8',
    '班級編號':'820221018212141',
    '評價分數':'10'}

data = requests.post(url,data=param,headers=header).text
print(data)