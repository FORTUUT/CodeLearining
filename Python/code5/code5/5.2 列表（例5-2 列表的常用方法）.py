#5.2 列表（例5-2 列表的常用方法）
#初始化3个列表
lst2=["python",12,2.71828,[0,0],12]
lst3=[21,10,55,100,2]
lst=['aaa','bbb']
#替换列表元素
lst2[2]=3.14; print(lst2)
lst2[0:3]=lst; print(lst2)
#追加（合并）列表
lst2+=lst3; print(lst2)
#删除0,1,2等3个列表元素
del lst2[:3];  print(lst2)
lst2.append(99); print(lst2)  #追加列表元素
lst4=lst2.copy(); print(lst4)  #复制列表
lst4.clear();  print(lst4)   #清除列表
#删除列表指定位置上的元素，并返回删除元素值
lst2.pop(6);  print(lst2); print(id(lst2))
lst2.reverse();  print(lst2);  print(id(lst2)) #翻转列表
lst2.sort();  print(lst2);  print(id(lst2))  #排序列表
