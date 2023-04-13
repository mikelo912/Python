# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:05:29 2023

@author: thewh
"""

#關鍵字引數

def city(area,name):
    print("居住區域:", area)
    print("姓名:", name)
    
city("David", "西區")

print()

city("中區","Peter")
print()

city(name="Mary", area="西屯區")

#city(name="Mike", 北區) 兩個值都是name會產生衝突

city("北區", name="John")