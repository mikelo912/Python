# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:37:54 2023

@author: thewh
"""

'''
作業:大樂透對獎
1.電腦開出1-49之間6個號碼(不可重複)
2.使用者可下注?注，由使用者輸入1-49，6個號碼不重複
3.對獎 顯示中了多少注(二個號碼即中獎)
'''

"""
1.電腦開出1-49之間6個號碼(不可重複) -->一維串列
"""
import random #帶入亂數函式庫
#print(random.random()) #產生亂數，變數名需和函式名一樣，原始型態為浮點數
bonus = []
for i in range(6):
    ans = random.randint(1,49) #隨機從1~49產生一個亂數整數
    #如果數字重複，重新產生
    if bonus.count(ans) > 0:
        ans = random.randint(1,49)
    #數字不重複就加入中獎獎號
    else:
        bonus.append(ans)
#print(random.choice(number)) #從ans序列隨機挑選一個值
    
"""
2.使用者可下注?注，由使用者輸入1-49，6個號碼不重複 -->二維串列
"""

user = []
num = int(input("請輸入要下多少注(自行選號):"))
for i in range(1,num+1):
    print('這是第{}注，請輸入號碼1~49，號碼不可重複'.format(i))
    for j in range(1,7):
        userNum = int(input('請輸入第{}注第{}個號碼'.format(i,j)))
        if user.count(userNum) > 0:
            print("號碼重複，請重新輸入其他號碼")


#對獎 顯示中了多少注(二個號碼即中獎)
'''
比較對獎號碼跟每一注號碼
確認是否有兩個以上相同的值
'''

