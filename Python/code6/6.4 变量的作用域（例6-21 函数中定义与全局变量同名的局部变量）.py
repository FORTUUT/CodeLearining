#6.4 变量的作用域（例6-21 函数中定义与全局变量同名的局部变量）
basis=100            #全局变量
def func3(x,y):
    basis=90         #与全局变量同名，但是局部变量，与全局变量无关
    sum=basis+x+y
    return sum

print("{:6.2f}".format(func3(75,62)))
print(basis)         #全局变量值仍为100
print("------------------------")
