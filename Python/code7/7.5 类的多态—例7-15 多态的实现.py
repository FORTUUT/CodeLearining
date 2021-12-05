#7.5 类的多态—例7-15 多态的实现
class Animal:
    def __init__(self,aname):
        self.name=aname
    def enjoy(self):
        print("nangnang")

class Cat(Animal):    #动物子类猫类
    def enjoy(self):  #根据猫的特征重写enjoy方法
        print(self.name," miaomiao")

class Dog(Animal):    #动物子类狗类
    def enjoy(self):  #根据狗的特征重写enjoy方法
        print(self.name+" wangwang")
        
class Person:
    def __init__(self,id,name):
        self.name=name
        self.id=id
    def drive(self,ani):   #传入参数
        ani.enjoy()        #执行enjoy方法
           
cat=Cat("Mikey")
dog=Dog("Dahuang")
person=Person("zhang3",9)
person.drive(cat)          #传入参数为猫类对象猫，执行不同的enjoy效果
person.drive(dog)          #传入参数为狗类对象狗，执行不同的enjoy效果





