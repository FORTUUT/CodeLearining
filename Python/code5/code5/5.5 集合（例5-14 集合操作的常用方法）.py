#5.5 集合（例5-14 集合操作的常用方法）
#创建两个集合
aset=set("python");bset=set([1,2,3,5,2]);cset=bset.copy()
print(aset,bset,cset)
#向集合bset中添加元素"y"
bset.add("y");print(bset);bset.pop();print(bset)
#判断集合中是否存在重复元素
#如果集合bset中没有与aset共有的元素则返回 True。
#因集合bset与aset含有共有元素"y",返回False
print(bset.isdisjoint(aset));print(len(aset))
cset.clear();print(cset)   #清楚集合cset中所有元素
