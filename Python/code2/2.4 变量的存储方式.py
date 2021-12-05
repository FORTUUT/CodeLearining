#2.4 变量的存储方式
a=1;b=2
print("a=",a,"a的存储地址：",id(a))
print("b=",b,"b的存储地址：",id(b))
b=a
print("a=",a,"a的存储地址：",id(a))
print("b=",b,"b的存储地址：",id(b))