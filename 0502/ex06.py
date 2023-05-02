# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:03:32 2023

@author: USER
"""

#抽象的類別不能生成
from abc import ABCMeta,abstractclassmethod
class Person(metaclass = ABCMeta):
    @abstractclassmethod #未完成的方法
    def display(self,name):
        pass
    def pay(self):
        self.display(self.name,self.salary)
        
class Clerk(Person):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self, name, salary):
        print(name,'是客拉客')
        print('薪水:',salary)
        
Bill = Clerk('Bill',32000)
Bill.pay()
p = Person()