"""
python 一個程式檔 架構 三個元素

  class n個 n>=0
  def fun() n個 n>=0
  直接執行指令 n個 n>=0

這三個元素沒先後順序性

 但須注意往前參考因yhon 程式是直譯 不能預測未來時光

  python 函數文法:

  def 函數名(參數列) :
   縮排 函數實作 #空實作請用pass

  python 函數的參數列 特點
  有預設參數
   *arg ---->tuple
   **kargs  --->dict
 不是預設參數 則參數必須數格子,照格子順序填入
   
"""
def TestMethod1() :
    print("測試方法動作")

def EmptyImplementMethod() :
    #由子類別改寫 override
    pass
def normalArgsMethod(a , b):
    print(a,b)
def defaultArgMethod1(v1="沒給自動補設這個值" ) :
    print(v1)
def halfDefaultArgsMethod1(a,b="預設參數"):
    print(a)
    print(b)
TestMethod1()
defaultArgMethod1()
defaultArgMethod1("我自己給值不使用預設")
normalArgsMethod(5,6)#正確
normalArgsMethod(b=6,a=5)#python參數特點 key(索引鍵)=value(值),舉例 學號 = 學員資料

halfDefaultArgsMethod1("非預設參數")
halfDefaultArgsMethod1("非預設參數","改變b的值")
#halfDefaultArgsMethod1(b="改變b的值","非預設參數")#違反不是預設參數 則參數必須
halfDefaultArgsMethod1(b="改變b的值",a="非預設參數")

def plus(*num):#*num是唯讀的list
    print(type(num))
    result=0
    for v in num:
        result=result+v
    print(result)

plus(1,2,5,4)

def doubleStarArgs(**kwargs):
    for k,v in kwargs:
        print(k,v,sep='=')

dict1={'a':5,'b':6,'c':7}
doubleStarArgs(**dict1)
