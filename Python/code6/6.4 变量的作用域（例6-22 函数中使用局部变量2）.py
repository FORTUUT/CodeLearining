#6.4 变量的作用域（例6-22 函数中使用局部变量2）
basis=100            #全局变量
def func4(x,y):
    basis=90      #先定义局部变量
    print(basis)  #后使用与全局变量同名的局部变量
    sum=basis+x+y
    return sum
print(func4(78,62))
print(basis)
