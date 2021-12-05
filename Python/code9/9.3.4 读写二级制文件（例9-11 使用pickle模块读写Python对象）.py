#9.3.4 读写二级制文件（例9-11 使用pickle模块读写Python对象）
lst1=["read","write","tell","seek"]  #列表对象
dict1={"type1":"TextFile","type2":"BinaryFile"}  #字典对象
fileb=open(r"G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\mydata.dat",'wb')
#写入数据——写对象到文件
import pickle
pickle.dump(lst1,fileb)
pickle.dump(dict1,fileb)
fileb.close()
#读取数据——读对象到程序
fileb=open(r"G:\\2021-2022-1\\Python\\PPT\\ch9\\code9\\mydata.dat",'rb')
print(fileb.read())
print(fileb.seek(0))  #文件指针移动到开始位置
x=pickle.load(fileb)
y=pickle.load(fileb)
print(x,y)


