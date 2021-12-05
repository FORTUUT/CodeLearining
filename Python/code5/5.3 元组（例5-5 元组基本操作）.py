#5.3 元组（例5-5 元组基本操作）
tup1=('physics','chemistry',1997,2000) #元组中包含不同类型的数据
tup2=(1,2,3,4,5)
tup3="a","b","c","d"   #声明元组的括号可以省略
tup4=(50,)    #元组只有一个元素时，逗号不可省略
tup5=((1,2,3),(4,5),(6,7),9)
print(type(tup3),type(tup4)) #变量类型测试
print(1997 in tup1)
print(tup2+tup3)   #元组连接
print(tup1[1]);  print(max(tup3))
print(tup1.index(2000))   #检索元组中元素的位置
print(help(tuple))    #显示元组的属性和方法
print(tup3.index(2000))  #检索的元素不存在，运行报异常
