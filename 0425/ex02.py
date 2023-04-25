# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:15:07 2023

@author: USER
"""

class Account:
    def __init__(self,number,Acc): #初始化
        self.number = number
        self.account = Acc
        self.balance = 0
    def display(self):
        print('帳號:',self.number)
        print('戶名:',self.account)
    def deposit(self,money1):
        if money1 > 0:
            self.balance += money1
        else:
            raise RuntimeError('存錢必須為正整數')
            #print('存錢必須為正整數')
    def withDraw(self,money2):
        if self.balance >= money2:
            self.balance -= money2
        
print(__name__) #印出主程式名稱

a = Account('123-456-789', 'Mike')
a.display()
money = int(input('輸入存款金額:'))
if money <= 0:
    print('無法存錢')
else:
    a.deposit(money)
print('存款金額:',money)
print('帳戶餘額:',a.balance)
#a.withDraw(100)
#print('餘額:',a.balance)