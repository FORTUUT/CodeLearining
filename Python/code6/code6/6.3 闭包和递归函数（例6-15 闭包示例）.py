#6.3 闭包和递归函数（例6-15 闭包示例）
def greeting_conf(prefix):  #外部函数（函数嵌套）
    def greeting(name):     #内部函数，功能：打印prefix和name的值
        print(prefix, name)   #外部函数的参数prefix在内部函数中引用
    return greeting    #将内部函数的名称greeting作为外部函数的返回值

mGreeting = greeting_conf("Good Morning")
mGreeting("Wilber")
mGreeting("Will")
print()
#变量mGreeting指向greeting_conf函数，实际引用闭包函数greeting占用的内存空间
#利用mGreeting执行闭包函数greeting时，因还记得外层函数的作用域，不会释放变量prefix，
#因此可以将prefix（外层函数的变量）和name（自身变量）参数打印出来。
aGreeting = greeting_conf("Good Afternoon")
aGreeting("Wilber")
aGreeting("Will")
