#9.3.1 例9-2 读取文件数据（使用read()方法读取文本文件的内容）.py
f=open("test.txt","r")
str1=f.read(13)
print(str1)
str2=f.read()  #从文件当前指针处开始读取
print(str2)
f.close()


