#5.4 字典（例5-12 字典的常用方法copy与update)
dict1={"id":101,"name":"Rose","address":"Changjianroad"}
#copy()方法
dict2=dict1.copy()
print(id(dict1),id(dict2))
print(dict1 is dict2)
dict2["id"]=102
print(dict2)
print(dict1)
#update()方法
dict3={"name":"John","emial":"u1@u2"}
dict1.update(dict3)
print(dict1)