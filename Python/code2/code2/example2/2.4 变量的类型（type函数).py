#2.4 变量的类型(type函数)
#和Java不同，Python中变量在定义时不需要预先声明变量的类型
#Python会根据变量的值自动判断该变量的类型。
#当无法确认一个变量的类型时，使用type()函数查看变量类型。
a=1;b=1.1;c="hello"
print("变量a的类型：",type(a),"\n变量b的类型：",type(b),"\n变量c的类型：",type(c))

#已定义的变量类型并不是一直不变的，它会跟随对应的值类型的改变而改变。
e=10;print("变量e的类型：",type(e))
e=10.2;print("变量e的类型：",type(e))
e="world";print("变量e的类型：",type(e))