#4.4 流程控制的其他语句—跳转语句
#例4-11，continue语句示例。
#求输入数值中正数之和，负数忽略
s=0
for i in range(6):
    x=eval(input("请输入数值数据：  "))
    if x<0:continue
    s+=x
print("正数之和是： ",s)
