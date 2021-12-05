#9.3.1 读取文件数据（例9-5 以迭代方式读取文本文件的内容）
f=open("test.txt","r")
for line in f:
    print(line,end="")
f.close()

