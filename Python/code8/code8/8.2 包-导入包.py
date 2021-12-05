#8.2 包（导入包)
import mypackage
from mypackage import *
print("包mypackage的模块mymodule1中的x={}".format(mypackage.mymodule1.x))
mymodule1.testm1()
print("包mypackage的模块mymodule2中的y={}".format(mypackage.mymodule2.y))
mymodule2.testm2()

