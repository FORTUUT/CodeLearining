#6.3 闭包和递归函数（例6-16 求斐波那契数列第i个元素的递归函数）
def fib(i):
    if i==0:
        return 0                   #i=0的出口
    elif i==1:
        return 1                   #i=1的出口
    else:
        return fib(i-1)+fib(i-2)   #i>=2的出口

print(fib(8))