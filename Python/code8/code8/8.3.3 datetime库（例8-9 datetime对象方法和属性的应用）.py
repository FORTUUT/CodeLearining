#8.3.3 datetime库（例8-9 datetime对象方法和属性的应用）
from datetime import *
dt=datetime.today()
print("当前日期是{}年{}月{}日".format(dt.year,dt.month,dt.day))
print(dt.time())
tup1=dt.timetuple()
print(tup1)
print("当前日期是：{}年{}月{}日".format(tup1.tm_year,tup1.tm_mon,tup1.tm_mday))
print(dt.ctime())
print(dt.replace(month=12))

