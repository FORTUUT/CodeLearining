#6.2 函数的参数和返回值（例6-11 return关键字的应用）
def compare(arg1,arg2):
    "比较两个参数的大小"
    result=arg1>arg2
    return result   #函数体内result值
#调用compare函数
btest=compare(10,9.99)
print("函数的返回值：",btest)

