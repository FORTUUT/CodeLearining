#6.2 函数的参数和返回值（例6-6 基本数据类型作为实参）
a=10   #全局变量
def func(num):
    num+=1
    print("形参的地址{}".format(id(num)))
    print("形参的值{}".format(num))
    a=1    #局部变量，只在函数内部有效
func(a)
print(a,id(a)) #函数调用后，变量a的值不发生变化