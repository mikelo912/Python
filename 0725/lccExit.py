# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:22:27 2023

@author: USER
"""

#作業:到聯成電腦網頁抓取簽退的資料

import requests
from bs4 import BeautifulSoup

url = "https://member.lccnet.com.tw/"

header = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
    
param = {"Account":"105670139",
"Password":"A125218125",
"RememberMe":"false",
"__RequestVerificationToken":"F94kUTjV1vQ2Y33bJTo6dp7gxox3iFU4Twn-d-AkOwe3IdsOBUWNmunq96UwnU9P5LKdFtmiyOjDwMDlVM-P_L7K0KNRqRUpzgXXDEJheYA1"
}

