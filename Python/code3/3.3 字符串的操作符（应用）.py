#3.3 字符串的操作符（应用）
#例3-5 字符串操作符的应用
str1="Hi,Python!"  #str1重复显示2次，str1未发生改变
print(str1*2)
print(id(str1))    #测试str1在内存中的标识
str1+="Hi,Java!"
print(id(str1))    #str1连接字符串后，id发生改变
print(str1)
print(str1[3:9])   #字符串切片操作
print(str1[-5:-1]) #从后向前切片，最后一个字符索引是-1
print(str1[:-6])   #从索引为-6的字符到字符串首
print("java" in str1)   #False
print("Java" in str1)   #True