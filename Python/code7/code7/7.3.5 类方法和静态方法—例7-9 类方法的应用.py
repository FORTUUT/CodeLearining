#7.3.5 类方法和静态方法—例7-9 类方法的应用
class DemoClass2:
    def __init__(self,year=0,month=0,day=0):
        self.day=day
        self.month=month
        self.year=year
    @classmethod
    def get_date(cls,string_date):   #类方法
        #第一个参数cls， 表示调用当前的类名
        year,month,day=map(int,string_date.split('-'))
        date1=cls(year,month,day)  #调用构造方法
        return date1   #返回的是一个初始化后的该类对象
    def output_date(self):     #实例方法
        print("year:",self.year,"month:",self.month,"day:",self.day)
rq1= DemoClass2(2018,6,2)
rq1.output_date()
rq2=DemoClass2.get_date("2018-6-6")
rq2.output_date()

