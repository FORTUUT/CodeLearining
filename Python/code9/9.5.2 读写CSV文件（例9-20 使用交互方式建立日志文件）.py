#9.5.2 读写CSV文件（例9-20 使用交互方式建立日志文件）.py
from datetime import datetime
filename=input("请输入日志文件名：")
file=open(filename,'a')
print("请输入日志，exit结束")
s=input("log:")
while s.lower()!="exit":
    file.write("\n"+s)
    file.write("\n----------------------\n")
    file.flush()
    s=input("log:")
file.write("\n====="+str(datetime.now())+"=====\n")
file.close()
