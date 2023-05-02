# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:39:15 2023

@author: USER
"""

class A:
    def aMethod(self):
        print('aMethod')

class B(A):
    def bMethod(self):
        print('bMethod')
    def display(self):
        print('b-display')
    
class C(B):
    def cMethod(self):
        print('cMethod')
    def display(self):
        print('c-display')
        
class D(C,B):
    def dMethod(self):
        print('d-Method')
        
a = C()
a.aMethod()
a.bMethod()
a.display() #先使用類別C裡面的方法

d = D()
d.display()