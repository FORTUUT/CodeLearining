#7.3.5 类方法和静态方法—例7-10 静态方法的应用
class DemoClass3:
    def instancemethod(self):       #成员方法
        print("instance method")
    @staticmethod
    def staticmethod1():            #静态方法
        print("static method")
obj = DemoClass3()
obj.instancemethod()
obj.staticmethod1()
DemoClass3.staticmethod1()

