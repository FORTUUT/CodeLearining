#3.3 字符串的操作符（表3.3实例）
a="Hello";b="Python"
c=a+b;d=a*2
print("连接字符串输出：",c)
print("重复输出字符串：",d)
e=a[1];print("切片操作输出（索引获取）：",e)
f=a[1:4];print("切片操作输出（截取）：",f)
g='H' in a
h='M' not in a
print("字符串包含给定字符返回：",g)
print("字符串不包含给定字符返回：",h)
print("原始字符串：",r'\n')
print("返回二进制字符串：",b"123")

