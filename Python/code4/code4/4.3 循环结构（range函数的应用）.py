#4.3 循环结构（range函数的应用）
print(list(range(10)))   #从0到10的整数列表
print(list(range(1,11))) #从1到11的整数列表
print(list(range(0,30,5)))  #从0到30的整数列表，步长为5
print(list(range(0,10,3)))  #从0到10的整数列表，步长为3
print(list(range(0,-10,-1))) #从0到-10的整数列表，步长为-1

#Python2的range()函数返回一个列表
#Python3的range()函数返回迭代器，
#如果要查看列表，要用list()函数转换成列表