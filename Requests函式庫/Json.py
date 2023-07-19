# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:25:46 2023

@author: s9571
"""

import requests

#抓取json檔案內容
response = requests.get('https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON')
print(response.json())