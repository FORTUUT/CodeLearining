#5.3 元组（例5-6 元组与列表转换）
tup1=(123,'xyz','zara','abc')
lst1=list(tup1)
lst1.append(999)
print(lst1)
tup1=tuple(lst1)
print(tup1)