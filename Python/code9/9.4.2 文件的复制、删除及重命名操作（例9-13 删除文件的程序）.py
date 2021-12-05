#9.4.2 文件的复制、删除及重命名操作（例9-13 删除文件的程序）
import os,os.path
fname=input("请输入需要删除的文件名：")
if os.path.exists(fname):
    os.remove(fname)
    print("{}文件已经被删除".format(fname))
else:
    print("{}文件不存在".format(fname))

