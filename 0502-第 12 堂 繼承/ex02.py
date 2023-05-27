# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Father:
    def car(self):
        print('Father Car')
    
    def house(self):
        print('Father House')
        
class Mother:
    def car(self):
        print('Mother Car')
    def Clothes(self):
        print('漂亮的衣服')
        
class Son(Father,Mother): #繼承順序有先後
    def school(self):
        print('Son的學校:聯成分校')

s = Son()

s.Clothes()
s.car()
s.house()
s.school()