#9.3.2 向文件写数据（例9-6 向文件中写入字符串）
fname=input("请输入追加数据的文件名：")
f1=open(fname,"w+")
f1.write("向文件中写入字符串\n")
f1.write("继续写入")
f1.close()



