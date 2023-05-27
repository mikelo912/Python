# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:44:48 2023

@author: USER
"""

import random

data = set() #hashset 雜湊，略過重複項

while len(data) < 6:
    data.add(random.randint(1,49))
    
print(data)