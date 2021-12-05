#6.5 Python的内置函数（例6-35 type()和id()函数的应用）
lst1=[1,2,3]
lst2=lst1
lst3=lst1.copy()
print(id(lst1),id(lst2),id(lst3))
print(type([]))