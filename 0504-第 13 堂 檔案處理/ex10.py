# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:47:11 2023

@author: USER
"""

import os

myDir = "lcc"
if os.path.exists(myDir):
    #print('已存在')
    os.rmdir(myDir)
    print('已刪除')
else:
    os.mkdir(myDir)