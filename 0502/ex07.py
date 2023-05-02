# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:32:02 2023

@author: USER
"""

#動態紀錄 又叫做動態更換類別
class Father:
    def display(self,name):
        self.name = name
        print('Father Name is:',self.name)
        
class Mother:
    def display(self,name):
        self.name = name
        print('Mother Name is:',self.name)
        
class Child(Father, Mother):
    pass
class Son(Father):
    pass

print(Child.__name__,'繼承')
for i in Child.__bases__:
    print(i)
    
print(Son.__name__,'繼承')
print(Son.__bases__)

s = Son()
s.display('David')
Son.__bases__ = (Mother,) #更改繼承類別
s.display('Mary')