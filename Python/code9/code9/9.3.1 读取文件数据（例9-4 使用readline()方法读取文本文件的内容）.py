#9.3.1 读取文件数据（例9-4 使用readline()方法读取文本文件的内容）.py
f=open("test.txt","r")
str1=f.readline()     #readline读取一行

while str1!="":   #判断文件是否结束
    print(str1)   #字符串非空则打印
    str1=f.readline()  #循环读取一行
f.close()


