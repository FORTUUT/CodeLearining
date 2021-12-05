#6.1 函数的定义和调用（例6-2 函数调用和类型测试）
def getcirclearea(r):
    print("圆的面积是：{:>8.2f}".format(3.14*r*r))
    return
getcirclearea(3)
print(getcirclearea)   #函数名变量在内存中的地址
print(type(getcirclearea)) #返回getcirclearea的类型
print(getcirclearea(3))
# 在python中，函数名也是一个变量，
# return语句无返回值时，函数值为None,返回None