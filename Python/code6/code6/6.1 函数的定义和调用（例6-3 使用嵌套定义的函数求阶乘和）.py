#6.1 函数的定义和调用（例6-3 使用嵌套定义的函数求阶乘和）
def sum(n):
  def fact(a):   #嵌套函数，求阶乘
      t=1
      for i in range(1,a+1):
         t*=i
      return t
  s=0
  for i in range(1,n+1):
      s+=fact(i)    #调用嵌套函数fact()
  return s

n=5
print("{}以内的阶乘之和为{}".format(n,sum(n)))