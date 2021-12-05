#6.4 变量的作用域（例6-23 global语句的应用）
basis=100            #全局变量
def func4(x,y):
    global basis     #声明basis是函数外的全局变量
    print(basis)     #100
    basis=90
    sum=basis+x+y
    return sum
print(func4(75,62))
print(basis)          #90

