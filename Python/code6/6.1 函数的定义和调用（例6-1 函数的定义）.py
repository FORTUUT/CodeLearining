#6.1 函数的定义和调用（例6-1 函数的定义）
def hello():
    print("Hello Python!")
hello()
def getarea(x,y):
    '''
    参数为两个数值数据，或者一个字符串和一个整数
    '''
    return x*y
print(getarea(3.0,2.0))
print(getarea("hello",2))
print(help(getarea))
