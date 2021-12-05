#3.4 字符串处理函数（头尾判断）
#例3-9 字符串判断函数的应用
str1="hi,Python!hi,Java!"
print(str1.startswith("hi"))
print(str1.endswith("Java!"))
print(str1.startswith("hi",3)) #从str1的第3个字符开始判断，不以"hi"开头
print(str1.endswith("hi",3,12)) #判断str1的第3~12个字符，以"hi"结尾