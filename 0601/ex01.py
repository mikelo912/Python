# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sayHello(name):
    print(name,'你好')
    
sayHello('Bill')

def square(x):
    return x**2 #x的平方

print(square(5))

print('-'*30)
(lambda name:print(name,'你好'))('John') #lambda匿名函式
sq=lambda x:x**2
print(sq(5))

sq2=lambda x,y:x*y
print(sq2(2,5))