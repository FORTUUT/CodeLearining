#9.5.2 读写CSV文件（例9-16 将一维数据写入CSV文件并读取）.py
# 向CSV文件中写入一维数据并读取
lst1 = ["name","age","school","address"]
filew= open('asheet.csv','w')
str=",".join(lst1)   #以指定的字符串（逗号）作为分隔符，将所有元素合并为一个新的字符串
filew.write(str)
filew.close()
filer= open('asheet.csv','r')
line=filer.read()
print(line)
filer.close()



