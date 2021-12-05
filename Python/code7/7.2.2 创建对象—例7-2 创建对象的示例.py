#7.2.2 创建对象—例7-2 创建对象的示例
class Dog:
    num = 0              #类属性 
    def __init__(self,id=0,color="yellow"):#构造方法
        self.id=id
        self.color=color
    def enjoy(self):     #成员方法
        print("wangwang")
    def show(self,weight):
        print("重量{}公斤".format(weight))
        print("颜色{}".format(self.color))
dog =Dog(color="grey")
dog.weight=52
dog.show(dog.weight)
dog.enjoy()

