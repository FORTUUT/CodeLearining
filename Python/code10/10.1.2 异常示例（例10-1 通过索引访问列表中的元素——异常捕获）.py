# 10.1.2 异常示例（例10-1 通过索引访问列表中的元素——异常捕获）.py
try:
  weekday=["Mon","Tues","Wednes","Thurs","Fri","Satur","Sun"]
  print(weekday[2])
  print(weekday[7])
except IndexError:
  print("列表索引可能超出范围")


