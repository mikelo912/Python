# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json

import requests

def get_bike():
    url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=2000"
    
    data = requests.get(url).text
    
    bike = json.loads(data)
    
    #a = data['records'][]
    
    air = bike['records']
    msg = 'bike'
    for item in air:
        msg += item['sitename']+"-"+item['aqi']+"\n"
        i+=1
        if i == 6:
            break
        
    return msg

from attbike import getBike
