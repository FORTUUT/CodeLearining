#7.3.5 类方法和静态方法—例7-8 类中定义的实例方法和类方法
class DemoClass1:
    def instancemethod(self):      #实例方法
        print("instance method")
    @classmethod          
    def classmethod1(cls):         #类方法
        print("class method")
obj = DemoClass1()
obj.instancemethod()
obj.classmethod1()
DemoClass1.classmethod1()

