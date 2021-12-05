#7.3.4 成员变量和类变量—例7-7 定义含有成员变量和类变量的Animal类
class Animal:
    num=0      #类属性
    def __init__(self,aname,acolor):#构造方法
        self.name=aname      #实例属性
        self.color=acolor
    def show(self):          #成员方法，类属性用类名访问
        print("名字:{},颜色：{},数量：{}".format(self.name,self.color,self.num))
ani1 =Animal("fish","white")
ani2 =Animal("bird","green")
ani1.show()
ani2.show()
Animal.num=1  #通过类名修改类属性的值
ani1.num=2   #通过对象1修改类属性的值
ani2.num=3   #通过对象2修改类属性的值
ani1.show()
ani2.show()    
              

