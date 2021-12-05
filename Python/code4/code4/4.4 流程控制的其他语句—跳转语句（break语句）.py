#4.4 流程控制的其他语句—跳转语句
#例4-10，break语句示例。求99的最大真约数
a=eval(input("请输入的数值："))
i= a//2          #等价于i=int(a/2)
while i>0:
    if a%i==0: break
    i-=1
print(a,"的最大真约数为：",i)
