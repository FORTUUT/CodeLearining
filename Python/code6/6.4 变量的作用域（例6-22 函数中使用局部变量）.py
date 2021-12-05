#6.4 变量的作用域（例6-22 函数中使用局部变量）
basis=100            #全局变量
def func4(x,y):
    print(basis) #先使用与全局变量同名的局部变量异常
    basis=90
    sum=basis+x+y
    return sum
print(func4(78,62))
print(basis)

