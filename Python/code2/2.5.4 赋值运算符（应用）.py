#2.5.4 赋值运算符（应用）
#例2-10
x=5;           print(x)    #为一个变量赋值，x值为5
x=x+1;         print(x)  #x+1赋给x,值为6
x=y=z=5;       print(x,y,z)  #为多个变量赋一个值5
x,y,z=3,4,5;   print(x,y,z)  #为多个变量赋多个值3,4,5

#赋值运算和算术运算符组合成复合赋值运算符
a=5;b=3;a+=b;print(a)    #a=8
a=5;b=3;a-=b;print(a)    #a=2
a=5;b=3;a*=b;print(a)    #a=15
a=5;b=3;a/=b;print(a)    #a=1.6666666666666667
a=5;b=3;a%=b;print(a)    #a=2
a=5;b=3;a**=b;print(a)   #a=125
a=5;b=3;a//=b;print(a)   #a=1