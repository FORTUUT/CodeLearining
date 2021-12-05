# 10.2 Python异常类（例10-2 AttributeError异常示例）.py
class Person:
  sid = "01"

  def display():
    pass

p1 = Person()
p1.sname = "Rose"
print(p1.sid)
print(p1.sname)
print(p1.semail)






