"""
迴圈 第二種 while迴圈

  for each 往往用在 有限定次數的重複工作
  while 則用在沒有固定次數只有條件成立與否決定繼續執行

   if 條件:
      #

"""
"""
while True:
    print("=========")
"""
i=1
while i<10:
    j=1
    while j<10:
        if i*j>9 :
            print(" ",end="")
        else :
            print(end="  ")
        print(i*j,end="")
        j=j+1
    print("")
    i=i+1

"""
寫程式都是分化及克服
分化 把大問題切小
把小問題克服後大問題就解決了

 9*9乘法表第一個因是數字 1~9故就要考慮重複的工作, 重複工作就是利用迴圈
 j=1
 while j<10 :
     print(j,end=" ")
     j=j+1
============================
 i=1
 while i<10 :
     #這裡加上上面1~9的 while j程式碼
     i=i+1
     print("")

"""
