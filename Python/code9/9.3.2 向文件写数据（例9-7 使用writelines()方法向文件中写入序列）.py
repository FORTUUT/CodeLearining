#9.3.2 向文件写数据（例9-7 使用writelines()方法向文件中写入序列）
f1=open("G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\data7.dat","a")
lst=["HTML5","CSS3","Javascript"]
tup1=('2012','2010','1990')
m1={"name":"John","City":"SH"}
f1.writelines(lst)
f1.writelines('\n')
f1.writelines(tup1)
f1.writelines('\n')
f1.writelines(m1)
f1.close()

