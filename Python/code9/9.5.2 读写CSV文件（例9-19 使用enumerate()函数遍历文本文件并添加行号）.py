# 9.5.2 读写CSV文件（例9-19 使用enumerate()函数遍历文本文件并添加行号）.py
filename=input("请输入要添加行号的文件名：")
filename2=input("请输入新生成的文件名：")
sourcefile=open(filename,'r')
targetfile=open(filename2,'w')
linenumber=""
#enumerate将一个可遍历的数据对象(源文件)组合为一个索引序列，同时列出数据和数据下标
enu=enumerate(sourcefile)
for (num,value) in enu:#获得索引序列的索引号和数据值
    if num<9:
        linenumber='0'+str(num+1)
    else:
        linenumber=str(num+1)
    str1=linenumber+"   "+value
    print(str1,end="")
    targetfile.write(str1)
sourcefile.close()
targetfile.close()

