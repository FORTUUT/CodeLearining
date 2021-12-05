#8.3.3 datetime库（例8-10 strftime()方法的应用）
from datetime import datetime
dt1=datetime(2017,12,10,13,50)
dt2=datetime.today()
print(dt1.strftime("%Y-%m-%d"))
print(dt2.strftime("当前日期：%Y年 %m月 %d日,%A"))
print("当前日期：{0:%Y}年 {0:%m}月 {0:%d}日".format(dt2))

