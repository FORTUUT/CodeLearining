#4.3 循环结构（for循环示例1）
#计算1~100中能被3整除的数之和
s=0
for i in range(100):
    if i%3==0:
        s+=i
        print(i,end=" ")
print("\n","1~100中能被3整除的数之和为：",s)
