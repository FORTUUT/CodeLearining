#2.6 运算符的优先级（应用）
#例2-12
x=10;y=20;m=3.0;n=8.2

b=x+y>x-y*-1 and m<n%3
print(b)

b1=((x+y)>(x-y*(-1))) and m<(n%3)
print(b1)

b2=((x+y)>(x-y*(-1))) and (m<(n%3))
print(b2)