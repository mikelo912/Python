# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Clothes(object): #衣服的功能在裡面定義
    def water(self): #def是方法,self是物件本身
        print('衣服防潑水')
    def setColor(self,color): #color是區域變數
        self.color = color #第一個color是物件變數
        
if __name__ == '__main__':
    myClothes = Clothes()
    youClothes = Clothes()
    print(id(myClothes)) #id()是找出記憶體位置
    print(id(youClothes))
    
    myClothes.water()
    myClothes.setColor('紅色') #要先給值才可以使用
    youClothes.setColor('白色')
    print(myClothes.color)
    print(youClothes.color)