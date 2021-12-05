#4.4 流程控制的其他语句—二重循环中的else语句
#例4-14 在二重循环中使用else语句，
#查找50以内的质数并列表输出
num=[];i=2
for i in range(2,50):
   j=2
   # i能被2~i-1之间的数整除，则为非质数，跳出
   for j in range(2,i):
      if(i%j==0):
         break
   # 不能被2~i-1之间的数整除，为质数，插入列表
   else:
      num.append(i)
print(num)
