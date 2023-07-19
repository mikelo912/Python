# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:55:59 2023

@author: s9571
"""

import requests

web = requests.get('https://data.kcg.gov.tw/12345')
if web.status_code == 404:
    print('找不到網頁')