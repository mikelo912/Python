# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def displayScore(**score): #不定長度參數
    print('成績:',score)
    
displayScore(eng=72,python=81,math=99) #將參數帶入字典

def showScore(name,**score):
    print(name)
    print(score)
 
'''
showScore('Bill',eng=60)
'''

def students(title,**personal):
    print(title,"依姓名來排序:")
    for key in sorted(personal): #sorted預設是由小到大排序
        print("{0:8s}的分數{1}".format(key,personal[key])) 
        '''
        8s是字串保留8個位元
        {1}是抓出字典的value
        '''
    print('-'*30)
    
    low60 = {k:v for k,v in personal.items() if v <60} #字典表達式
    
    count = len(low60)
    print('不及格有:',count,'人')
    print(low60)
    
students("111年度第一次評量",Mary=61,Bill=63,Peter=99,Mike=44)

