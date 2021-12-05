#8.1.3 执行模块（例8-4 使用from语句导入模块时，模块中变量的变化情况）
from mymodule import *  #模块from导入后被自动执行，但只执行一次
print("x={}".format(x))
testm()
x=100
from mymodule import *
print("x={}".format(x))  #再次使用from语句导入模块后，x的值为最初模块文件中的初值
#这是使用import语句导入和使用from语句导入的一个重要区别

