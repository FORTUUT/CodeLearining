#2.4 变量的类型(isinstance函数)
#和Java不同，Python中变量在定义时不需要预先声明变量的类型
#Python会根据变量的值自动判断该变量的类型。
#当无法确认一个变量的类型时，也可以使用isinstance()函数查看变量类型
#返回结果为True或False。
a=1
b=1.1
c="hello"
print(isinstance(a,float))
print(isinstance(b,float))
print(isinstance(c,str))
