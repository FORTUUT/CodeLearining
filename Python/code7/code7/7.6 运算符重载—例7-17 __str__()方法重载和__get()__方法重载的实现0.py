# 7.6 运算符重载—例7-17 __str__()方法重载和__get()__方法重载的实现0.py
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Rose",17)
s2=Student("John",19)
print("学生s1：",s1)
print("学生s2：",s2)
#未运算符重载时打印的是对象的地址，
# 但希望打印对象的描述信息，需要重载__str__()和__get()__方法

