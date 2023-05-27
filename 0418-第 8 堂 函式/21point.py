# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:00:28 2023

@author: USER
"""


import random

'''
52張牌
每個點數都有4張
'''

cards = list() #52張牌
for i  in range(1,14): #1~13點，不超過14
    for y in range(1,5):
        cards.append(i)
#print(cards)，未洗牌前



#洗牌
def washCard(cards):
    for i in range(200):
        first = random.randint(0,len(cards)-1) #52張牌，索引值要-1
        end = random.randint(0,len(cards)-1)
        cards[first], cards[end] = cards[end],cards[first] #將first及end的牌倆倆交換


#發牌，開始遊戲
def giveCards():
    point = cards.pop(0)
    if point >= 10:
        point = 10
    return point

washCard(cards)
#print(cards)，洗牌後的牌堆

print('歡迎來到21點')
print('-'*30)
myMoney = 100
while myMoney > 0:
    coin = myMoney
    while True:
        coin = int(input('押注代幣:'))
        if coin > myMoney: #coin是押注代幣,myMoney是手上有的代幣
            print('代幣不足,目前代幣:',myMoney)
        else:
            break
    print('你下注代幣:',coin)

    NPC = list() #宣告為列表
    player = list()
    
    NPC.append(giveCards())
    print('莊家第一張牌:')
    player.append(giveCards())
    print('玩家第一張牌:',player[0],'點')
    
    print('-'*30)
    NPC.append(giveCards())
    print('莊家第二張牌:',NPC[1],'點')
    player.append(giveCards())
    print('玩家:',player[1],'點')
    
    print('目前玩家總點數:',sum(player)) #將列表內的值做加總
    print('-'*30)
    q = 'y'
    i = 2
    while q == 'y':
        q = input('請問要加牌嗎?(y/n)')
        if q != 'y':
            break
        player.append(giveCards())
        print('玩家:',player[i],'點')
        print('目前玩家總點數:',sum(player)) #將列表內的值做加總
        i+=1
        
        if sum(player) > 21:
            print('玩家爆了')
            break
        if sum(player) == 21:
            break
    
    print('莊家總點數:',sum(NPC))
    
    if sum(player) < 21:
        j=2
        while sum(NPC) <= 19:
            NPC.append(giveCards())
            print('莊家第',j,'張牌:',NPC[j],'點')
            print('莊家總點數:',sum(NPC))
            j+=1
    
    if sum(player) < 21:
        if sum(NPC) > 21 or sum(NPC) < sum(player):
            myMoney += coin
            print('玩家贏了',coin,'代幣')
        elif sum(NPC) == 21 or sum(NPC) > sum(player):
            myMoney -= coin
            print('莊家贏了,玩家減少',coin,'代幣')
    elif sum(NPC) == sum(player):
        myMoney -= coin
        print('莊家贏了,玩家減少',coin,'代幣')
    
    elif len(player) == 5 and sum(player) <= 21:
        myMoney += coin
        print('玩家過五關,贏了',coin,'代幣')
    
    elif len(NPC) == 5 and sum(NPC) <= 21:
        myMoney -= coin
        print('莊家過五關,玩家輸了',coin,'代幣')
    
    elif sum(player) > 21:
        myMoney -= coin
        print('玩家輸了,減少',coin,'代幣')
        
    elif sum(player) == 21:
        myMoney += coin
        print('玩家贏了',coin,'代幣')
        
        
    
    print('目前玩家剩餘:',myMoney,'元')
    q = input('繼續請按y:')
    if q !='y':
        break