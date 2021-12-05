#7.4.1 继承的实现—例7-12 类的继承的应用
class Employee:
    def __init__(self,name="",department="computer",age=20):
        self.setName(name)
        self.setDepartment(department)
        self.setAge(age)
    def setName(self,name):
        if type(name)!=str:
            print("姓名必须是字符")
            return
        self.__name=name
    def setDepartment(self,department):
        if department not in ["computer","communication","electric"]:
            print("专业必须是computer、communication或electric")
            return
        self.__department=department
    def setAge(self,age):
        if type(age)!=int or age>=33 or age<20:
            print("年龄必须是数字，且界于20至33之间")
            return
        self.__age=age
    def show(self):
        print("姓名：{} 专业：{} 年龄：{}".
              format(self.__name,self.__department,self.__age))
class ProjectManager(Employee):
    def __init__(self,name='',department="computer",age=22,title="middle"):
        Employee.__init__(self,name,department,age)  #子类的构造方法中调用了父类的构造方法
        self.setTitle(title)
    def setTitle(self,title):
        self.__title=title
    def show(self):
        Employee.show(self)  #子类的成员方法show()中调用了父类的成员方法show()
        print("职称：{}".format(self.__title)) #带双下划线的属性只能在类的内部访问，实现类的封装
try:
    emp1=Employee("Rose")
    emp1.show()
    pm1=ProjectManager("Mike","electric",26,"high")
    pm1.setAge(30)          #实例调用从父类继承的成员方法
    pm1.show()              #实例调用子类自己的成员方法
except Exception as ex:
    print("数据出现错误",ex)

