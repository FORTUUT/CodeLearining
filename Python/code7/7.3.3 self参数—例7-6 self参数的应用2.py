# 7.3.3 self参数—例7-6 self参数的应用.py
class Animal:
    '''
    类中未定义构造方法，使用默认的构造方法
    def __init__(self):
        self.color=color
    '''
    num = 0              #类属性
    # enjoy()方法没有self参数，普通的方法，由类名调用
    def enjoy():     
        print("wangwang")
    # show()方法使用self参数，成员方法
    def show(k,args): #成员方法的第1个参数通常命名为self，但使用其他参数名也是合法的。

        print("重量{}公斤".format(args))
ani =Animal()
ani.weight=52
Animal.enjoy()    #ani.enjoy()错误
ani.show(ani.weight)



              
              

