# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:01:14 2023

@author: USER
"""

import re

text = "John 在上課，在上課喝Drink 很快樂"
result = re.search("(.*) 在上課，在上課喝([A-Za-z]*)",text)

print(result.group()) #印出符合規則的字串
print(result.groups())