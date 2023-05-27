# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:08:02 2023

@author: USER
"""

#不可變的型別：整數, 字串, 元組
#可變的型別：串列, 字典
#淺複製：不可變型別去改變它時不會受影響
#深複製：對於不可變及可變的型別，去改變它時都不受影響

import copy

list1 = [1,2,3,4,5]
list2 = [1,[2,3]]
newlist1 = copy.copy(list1)
newlist2 = copy.copy(list2)
list1[0] = 100
print(list1)
print(newlist1)
list2[1][0] = 100
print(list2)
print(newlist2)

newlist3 = copy.deepcopy(list1)
newlist4 = copy.deepcopy(list2)
list2[1][1] = 99
print(list2)
print(newlist4) #deepcopy的關係，值不會被改變

