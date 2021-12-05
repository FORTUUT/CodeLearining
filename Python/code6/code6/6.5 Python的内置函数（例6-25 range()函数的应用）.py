#6.5 Python的内置函数（例6-25 range()函数的应用）
r1=range(10)  #从0开始到9
print(list(r1))
r2=range(1,11)  #从1开始到10
print(list(r2))
r3=range(0,10,3) #步长为3
print(list(r3))
r4=range(0,-10,-1) #步长为负数
print(list(r4))
print(type(r4))  #range类型