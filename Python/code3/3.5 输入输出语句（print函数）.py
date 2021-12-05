#3.5 输入输出语句（print函数）
#例3-13 print()函数的使用
x,y,z=100,200,300
print(x,y,z)  #print()函数中多个参数用逗号分隔
print(x,y,z,sep="##")   #设置print()函数的输出分隔符为##
print(x);print(y);print(z)  #3个print()语句，默认分行显示
print(x,end=" ");print(y,end=" ");print(z) #print()设置end参数，用空格分隔，不换行
f1=open("file.txt","w")   #可写方式打开一个文件
print(x,y,z,sep=",",end=" ",file=f1)   #打印x,y,z的值到文件，分隔符为逗号