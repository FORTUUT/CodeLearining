#6.2 函数的参数和返回值（例6-8 默认参数的应用）异常
def showmessage(age=18,name):
    "打印任何传入的字符串"
    print("姓名: ", name)
    print("年龄: ", age)
    return


# 调用showmessage函数
showmessage(age=19, name="Kate")
print("------------------------")
showmessage(name="John")