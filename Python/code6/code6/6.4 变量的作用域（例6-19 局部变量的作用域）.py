#6.4 变量的作用域（例6-19 局部变量的作用域）
def func1(x,y):
    x1=x
    y1=y
    z=100
    print("in func1(),x1=",x1)
    print("in func1(),y1=",y1)
    print("in func1(),z=",z)
    func2()
    return
def func2():
    x1=10
    y1=20
    z=0
    print("in func2(),x1=",x1)
    print("in func2(),y1=",y1)
    print("in func2(),z=",z)

func1('a','b')
