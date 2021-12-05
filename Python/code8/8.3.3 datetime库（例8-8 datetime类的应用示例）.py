#8.3.3 datetime库（例8-8 datetime类的应用示例）
from datetime import datetime
aday=datetime.now()
aday
print(aday)
dt1=datetime(2018,2,10,13,50)
dt1
print(dt1)
print(type(dt1))  #测试dt1类型
t1=dt1.time()
print(type(t1))   #测试t1类型
print("当前时间是{}:{}:{}".format(dt1.hour,dt1.minute,dt1.second))
