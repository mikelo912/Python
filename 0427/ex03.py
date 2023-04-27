# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:17:14 2023

@author: USER
"""

class myBirth:
    def __init__(self,name,y,m,d):
        self.name = name
        self.year = y
        self.month = m
        self.day = d
        
    def __str__(self):
        print(self.name,'你好')
        return '生日:'+str(self.year)+'年'+str(self.month)+'月'+str(self.day)+'日'
    
    def __repr__(self):
        return '{}年{}月{}日'.format(self.year,self.month,self.day)
        
        
birth = myBirth('Bill', 1999, 9, 21)
print(birth)
print(repr(birth))