#9.3.4 读写二级制文件（例9-10 向二进制文件读写bytes字符串)
#以'wb'方式打开二进制文件
fileb=open(r"G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\mydata.dat",'wb')
print(fileb.write(b"Hello Python"))  #写bytes字符串
n=123
print(fileb.write(bytes(str(n),encoding='utf-8')))  #将整数转换为bytes字符串写入文件
print(fileb.write(b"\n3.14"))
fileb.close()
#以'rb'方式打开二进制文件
file=open(r"G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\mydata.dat",'rb')
print(file.read())
file.close()
#以'r'方式打开二进制文件
filec=open(r"G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\mydata.dat",'r')
print(filec.read())
filec.close()

