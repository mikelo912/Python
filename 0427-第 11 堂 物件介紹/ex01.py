# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
    
    def getName(self):
        return self.__name
    
class Dancer:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
    
    def fight(self):
        print(self.__name,'使出森巴舞')
        
    def skill(self):
        print(self.__name,'使出百花撩亂')
    
    def cure(self):
        print(self.__name,'使出補血')
    
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
    
    def getHp(self):
        return self.__hp
    
    def getName(self):
        return self.__name

class Adviser:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name,'使出扇子攻擊')
        
    def skill(self):
        print(self.__name,'使出火龍計')
    
    def cure(self):
        print(self.__name,'使出補血')
        
    def trick(self):
        print(self.__name,'水淹七軍')
    
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
    
    def getHp(self):
        return self.__hp
    
    def getName(self):
        return self.__name        