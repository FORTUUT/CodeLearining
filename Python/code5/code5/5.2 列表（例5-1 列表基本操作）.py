#5.2 列表（例5-1 列表基本操作）
lst1=[]  #创建空列表
lst2=["python",12,2.71828,[0,0],12] #创建由不同类型元素组成的列表
lst3=[21,10,55,100,2]
print("字符串是否在列表2中？","python" in lst2)
print("切片访问列表中元素",lst2[3])          #通过切片访问列表中的元素
print("正向切片访问列表中元素",lst2[1:4])        #通过切片访问列表中的元素
print("反向切片访问列表中元素",lst2[-4:-1])      #通过切片访问列表中的元素
print("列表2长度为：",len(lst2)) #计算列表长度
print("检索列表中的元素：",lst2.index(12)) #检索列表中的元素
print("计算列表中出现元素的次数:",lst2.count(12)) #计算列表中出现元素的次数
print("计算列表中的最大值：",max(lst3))   #计算列表中的最大值