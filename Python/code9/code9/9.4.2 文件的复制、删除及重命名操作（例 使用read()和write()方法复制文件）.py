#9.4.2 文件的复制、删除及重命名操作（例 使用read()和write()方法复制文件）
f1=open("test.txt","r")
f2=open("test3.txt","w")
flist=f1.readlines()
f2.writelines(flist)
f2.close()
f1.close()
f2=open("test3.txt","r")
print(f2.read())

f1=open("test.txt","r")
f3=open("test4.txt","w")
str=f1.read()
f3.write(str)
f3.close()
f1.close()
f3=open("test4.txt","r")
print(f3.read())


