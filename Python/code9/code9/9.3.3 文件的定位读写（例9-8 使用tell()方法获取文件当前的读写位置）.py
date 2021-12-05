#9.3.3 文件的定位读/写（例9-8 使用tell()方法获取文件当前的读/写位置）
file=open("G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\test2.txt", 'r+')
str1=file.read(6)  #读取6个字符
print(str1)
print(file.tell())  #文件当前位置
print(file.readline())  #从当前位置读取本行信息
print(file.tell())  #文件当前位置
print(file.readlines())
print(file.tell())    #文件长度为87字节
file.close()

