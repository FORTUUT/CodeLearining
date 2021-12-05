#program0702.py
f=open("test.txt","r")
str1=f.read(13)
print(str1)
str2=f.read()  #从文件当前指针处开始读取
print(str2)
f.close()
