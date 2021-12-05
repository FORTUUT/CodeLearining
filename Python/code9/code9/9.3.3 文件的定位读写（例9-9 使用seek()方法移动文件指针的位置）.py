#9.3.3 文件的定位读/写（例9-9 使用seek()方法移动文件指针的位置）
file=open("G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\test2.txt","r+")
print(file.seek(6))  #移动当前指针至第6个位置
str1=file.read(8)
print(str1)
print(file.tell())   #当前指针在第15个位置
print(file.seek(6))  #重新移动当前指针至第6个位置
print(file.write("@@@@@@@")) #写入7个字符，覆盖掉原来数据
print(file.seek(0))  #当前指针移至第0个位置
print(file.readline()) #显示一行数据

