# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:50:26 2023

@author: USER
"""

class Account:
    def __init__(self,number,Acc): #初始化
        #物件變數私有化，只能在這個類別存取
        self.__number = number
        self.__account = Acc
        self.__balance = 0
    
    def display(self):
        print('帳號:',self.__number)
        print('戶名:',self.__account)
    
    def deposit(self,money1):
        if money1 > 100000:
            self.__balance += money1
            self.__interest() #物件封裝
        else:
            raise RuntimeError('存錢必須為正整數')
            #print('存錢必須為正整數')
    
    def withDraw(self,money2):
        if self.__balance >= money2:
            self.__balance -= money2
            
    def getBalance(self):
        return self.__balance
    
    def __interest(self):
        interest = self.__balance * 0.002
        self.__balance += interest
            
if __name__ == '__main__':
    a = Account('123-456-789', 'Mike')
    a.display()
    a.__balance = 1 #動態建立變數，與內部私有化不同
    #print('帳戶餘額:',a.__balance)
    print(a.getBalance())
    a.deposit(100005)
    print(a.getBalance())