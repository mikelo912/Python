# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:29:10 2023

@author: USER
"""

class SwordsMan:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
    
    def fight(self):
        print(self.__name,'使出三刀流')
        
    def skill(self):
        print(self.__name,'使出星爆氣流斬')
        
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
    
    def getHp(self):
        return self.__hp
    
class Dancer:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
    
    def fight(self):
        print(self.__name,'使出XXX')
        
    def skill(self):
        print(self.__name,'使出OOO')
    
    def cure(self):
        print(self.__name,'使出補血')
    
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
    
    def getHp(self):
        return self.__hp