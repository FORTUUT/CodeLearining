#8.1.3 执行模块（例8-3 使用import导入模块观察模块中变量变化）
import mymodule    #模块import导入后被自动执行，但只执行一次
print("x={}".format(mymodule.x))#导入模块时，Python使用模块文件创建一个模块对象，模块中对象的变量名为对象属性
mymodule.testm()
mymodule.x=100
help(mymodule)  #使用help()函数可查看模块中对象的属性信息
print(dir(mymodule)) #Python为模块对象添加了内置属性，dir()函数列出模块属性列表，
                     # __开头和结尾的是内置属性，其他为变量名
import mymodule    #再次import导入统一模块，模块不会再执行，只重新建立到已经创建对象的引用
temp=mymodule      #模块中的打印语句在第2次导入时也没有执行
print("x={}".format(temp.x))      #import重新导入模块并未改变内存中模块变量x已有的赋值
temp.testm()

