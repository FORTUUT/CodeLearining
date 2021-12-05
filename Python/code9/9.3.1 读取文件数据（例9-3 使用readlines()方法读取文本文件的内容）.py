#9.3.1 读取文件数据（例9-3 使用readlines()方法读取文本文件的内容）.py
f=open("test.txt","r")
flist=f.readlines()       # readlines读取多行，flist是包含文件内容的列表
print(flist)
for line in flist:
    print(line)                  # 每行都有换行符，打印语句也包含换行，则有空行。

for line in flist:
    print(line,end="")           #使用print(line,end="")将不显示文件中的空行。
f.close()

