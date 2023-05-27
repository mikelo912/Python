# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:12:10 2023

@author: USER
"""

from ex01 import Adviser,Dancer,SwordsMan
import random

if __name__ == '__main__':
    print('歡迎來到online三國')
    player = list()
    com = list()
    
    while len(player) < 2:
        num = int(input('請選擇職業,1劍士, 2舞者, 3軍師:'))
        if 0 < num < 4:
            name = input('輸入角色姓名:')
            if num == 1:
                player.append(SwordsMan(name,100,1))
            elif num == 2:
                player.append(Dancer(name,100,1))
            else:
                player.append(Adviser(name,100,1))
                
    role = ['張飛','關羽','劉備','曹操','孫權','貂蟬']
    while len(com) < 2:
        num = random.randint(1,3)
        name = random.choice(role)
        print('電腦',len(com)+1,'號:',name)
        if num == 1:
            com.append(SwordsMan(name,100,1))
        elif num == 2:
            com.append(Dancer(name,100,1))
        else:
            com.append(Adviser(name,100,1))
            
    n = 1
    while len(player) > 0 and len(com) > 0:
        number = random.randint(1,100)
        print('第',n,'回合')
        if number % 2 == 0:
            p = player[random.randint(0,len(player)-1)]
            c = com[random.randint(0,len(com)-1)]
            
            if isinstance(p,Adviser):
                p.trick()
            else:
                p.fight()
                        
            print('打向',c.getName())
            blood = c.changeHp(random.randint(1,10))
            print('剩餘血量:',blood)
            n += 1
            if blood <= 0:
                print(c.getName(),'死了')
                com.remove(c)
        else:
            p = player[random.randint(0,len(player)-1)]
            c = com[random.randint(0,len(com)-1)]
            c.fight()
            print('打向',p.getName())
            blood = p.changeHp(random.randint(1,10))
            print('剩餘血量:',blood)
            n += 1
            if blood <= 0:
                print(p.getName(),'死了')
                player.remove(p)
    
    if len(player) > 0:
        print('玩家贏')
    else:
        print('電腦贏')