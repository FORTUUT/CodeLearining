#4.5 流程控制语句的应用——输出数字金字塔
#例4-17 输出数字金字塔
n=eval(input("请输入打印的行数： "))
for x in range(1,n+1):  #逐行打印
    print(' '*(10-x),end="")  #打印本行数字前的空格
    n=x
    while n>=1:    #第一个while循环，递减打印数字
        print(n,sep="",end="")  #空格隔开
        n-=1       #n自减1
   
    n=2
    while n<=x:    #第二个while循环，递增打印数字
        print(n,sep="",end="")  #空格隔开
        n+=1       #n自增1
    print()        #换行
