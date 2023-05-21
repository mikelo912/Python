"""
python 迴圈 loop 做重複的事
 for each 文法

 for  v   in  容器:
     處理v
 range()是一個提供一堆數字的函數,形式如下
   range(10) 代表提供 0到9數字(不含10)
   range(1,10) 代表提供 1到9數字(不含10)
   range(1,10,2) 代表提供 1到9數字(不含10), 但每次間隔2
 print() 方法文法參數:
    參數 sep="." sep 代表分隔符號
    參數 end="" end 代表結尾要加什麼字串,沒有end參數代表直接跳行
"""
#print(123,"abc",sep=".",end="")
#print("python presale course")
for m in (range(1,10)):
    for v in (range(1,10)) : #這是印出橫排
     #print(m*v,end=" ")
        if m*v>9 :
            print(" ",end="")
        else :
            print("  ",end="")
        print(m*v,end="")
    print("")

