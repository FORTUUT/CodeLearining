#6.2 函数的参数和返回值（例6-5 使用赋值参数计算总分）
def getscore(pe,eng,math,phy,chem):
    return pe*0.5+eng*1+math*1.2+phy*1+chem*1

print(getscore(93,89,78,89,72))  #按位置传递
print(getscore(pe=93,math=78,chem=72,eng=89,phy=89))  #使用赋值参数
