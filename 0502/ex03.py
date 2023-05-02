# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:19:46 2023

@author: USER
"""

class Role:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    
    def fight(self):
        print('角色攻擊')
        
    def display(self):
        print('姓名:',self.name)
        print('血量:',self.hp)
        
class Adivser(Role):
    def fight(self): #重新定義(覆寫 override)
        print('軍師扇扇攻擊')
    
    def cure(self):
        print('軍師補血大作戰')
        
class Swordman(Role):
    def fight(self):
        print('大劍一砍')
        
if __name__ == '__main__':
    a = Adivser('Mike',200)
    s = Swordman('關羽', 500)
    
    a.fight()
    a.cure()
    a.display()
    s.display()