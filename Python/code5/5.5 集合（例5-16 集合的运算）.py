#5.5 集合（例5-16 集合的运算）
aset=set([10,20,30])
bset=set([20,30,40])
set1=aset&bset   #交集运算
set2=aset|bset   #并集运算
set3=aset-bset   #差集运算
set4=aset^bset   #补集运算
print(set1);print(set2)
print(set3);print(set4)
print(set1<aset)  #子集测试
print(set2>aset)  #超集测试