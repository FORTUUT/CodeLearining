#5.4 字典（例5-10 字典的常用方法）
dicts={"id":101,"name":"Rose","address":"Changjianroad","pcode":"116022"}
#获得键的视图
key1=dicts.keys();print(type(key1))
key1=dicts.keys()
for k in key1:
    print(k,end=",")
print()
#获得值的视图
value1=dicts.values();print(type(value1))
for v in value1:
    print(v,end=",")
print()
#获得键值对的视图
items=dicts.items();print(type(items))
for item in items:
    print(item,end=",")