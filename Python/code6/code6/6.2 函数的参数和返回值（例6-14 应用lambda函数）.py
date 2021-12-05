#6.2 函数的参数和返回值（例6-14 应用lambda函数）
lst1=[3,5,-4,-1,0,-2,-6]
#lst2=sorted(lst1,key=lambda x:abs(x),reverse=True)
lst2=sorted(lst1,key=lambda x:abs(x))
#即：此匿名函数根据列表lst1中的数据的绝对值的大小进行排序
print(type(lst2))
print(lst2)
#说明：
#sorted()第1个参数：iterable可迭代对象——列表lst1
#sorted()第2个参数：key——主要用来进行比较的元素，指定接收一个参数的函数，
# 该函数的参数取自于可迭代对象中，指定可迭代对象lst1中的一个元素进行排序。
# 即，该函数用于从每个元素中提取一个用于比较的关键字
# 该处key使用lambda匿名函数，自定义函数，设置排序依据（对lst1的数取绝对值)
#sorted()第3个参数：reverse，控制排序升序（reverse=False默认）或降序（reverse=True）
#传递给key的lambda函数将给出正在排序的每个项，并返回Python可以按其排序的“键”。