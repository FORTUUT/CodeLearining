#9.4.3 文件的目录操作（例9-15 常用的目录操作命令）
import os
print(os.getcwd())  #查看当前目录
print(os.listdir())  #查看当前目录中的文件
os.mkdir('myforder')  #创建目录
os.makedirs('yourforder/f1/f2')  #创建多级目录
os.rmdir('myforder') #删除目录
#os.removedirs('yourforder/f1/f2') #直接删除多级目录
os.makedirs('aforder/ff1/ff2')  #创建多级目录
import shutil
shutil.rmtree('yourforder')  #删除存在内容的目录

