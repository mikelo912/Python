# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:29:53 2023

@author: USER
"""

scores = [60,70,65,100,91,88,65,81]
search = 65
start = 0

for i in range(scores.count(search)):
    index = scores.index(search,start+1)
    print("索引值:",index)
    start = index + 1