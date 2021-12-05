#6.5 Python的内置函数（例6-24 all()函数和any()函数的应用）
print(all([1,2]))  #列表中每个元素逻辑值均为True,返回True
print(all([0,1,2])) #列表中元素0的逻辑值为False,返回False
print(all(()))  #空元组
print(all({}))  #空字典
print(all(""))  #空字符串
print(all([]))  #空列表
print(any([0,1,2]))  #列表元素有一个为True,则返回True
print(any([0,0]))  #列表元素全部为False,则返回False
print(any([]))  #空列表