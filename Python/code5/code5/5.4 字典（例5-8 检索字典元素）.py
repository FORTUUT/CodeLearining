#5.4 字典（例5-8 检索字典元素）
dict={"id":101,"name":"Rose","address":"Changjianroad","pcode":"116022"}
print("id" in dict)
print("address" in dict)
print("Rose" in dict)
print(dict["id"])
print(dict["pcode"])
t1=dict["id"],dict["pcode"]
print(t1,type(t1))