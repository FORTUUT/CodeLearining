#6.5 Python的内置函数（例6-31 reversed()函数的应用）
r1=range(10)
r2=reversed(r1)  #r2是反转的可迭代对象
print(type(r2))
print(list(r2))