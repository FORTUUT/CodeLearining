#6.3 闭包和递归函数（例6-18 阶乘的递归实现）
def factorial(i):
    if i==0:
        return 1
    else:
        return i*factorial(i-1)

print(factorial(6))