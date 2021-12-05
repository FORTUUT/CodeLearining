#5.4 字典（例5-11 字典的常用方法get()与pop())
dicts={"id":101,"name":"Rose","address":"Changjianroad"}
#get()方法
print(dicts.get("address")) #获得address键对应的值
print(dicts.get("pcode"))#获得address键对应的值，无pcode键返回none
print(dicts.get("pcode","116000"))#pcode在字典中不存在，返回默认值
print(dicts)
print(dicts.pop('name'))#删除name键，返回对应的值Rose
print(dicts)            #删除name键值对后的字典
print(dicts.pop("email","u1@u2"))#email在字典中部存在，返回默认值
print(dicts)
dicts={"id":101,"name":"Rose","address":"Changjianroad"}
#使用popitem()函数逐一删除键值对
print(dicts.popitem())#删除一项键值对后的字典
print(dicts.popitem())#删除二项键值对后的字典
print(dicts.popitem())#删除三项键值对后的字典
print(dicts)