#7.2.1 创建类—例7-1 创建类的示例
class Dog:
    num = 0              #类属性/类变量
    def __init__(self,id=0,color="yellow"):#构造方法
        self.id=id
        self.color=color    #对象属性（对象特征）/成员变量
        
    def enjoy(self):     #对象方法（对象行为）/成员方法
        print("wangwang")
dog = Dog()
dog.enjoy()
print("类名访问类变量num={},对象名访问类变量num={}".format(Dog.num,dog.num))
print("对象名访问成员变量id={},对象名访问成员变量color={}".format(dog.id,dog.color))

