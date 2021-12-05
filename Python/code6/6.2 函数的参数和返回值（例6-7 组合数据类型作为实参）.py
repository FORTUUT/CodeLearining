#6.2 函数的参数和返回值（例6-7 组合数据类型作为实参）
#计算序列中的奇数，保存到参数ls1中
tup=(1,5,7,8,12,9)   #定义元组
ls=[]                #定义列表
def getodd(tup1,ls1):  #参数为组合数据类型
    for i in tup1:
        if i%2:
            ls1.append(i) #遍历元组的数据，偶数放入列表中
    return ls
print(ls)
print(getodd(tup,ls)) #函数调用前后，ls的值发生了变化，但id值不变
print(ls)