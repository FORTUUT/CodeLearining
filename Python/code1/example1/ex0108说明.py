# program0108.py
lst=[89,45,-34,23.1,98,33] #——列表数据赋值输入
maxscore=max(lst)     #调用函数获得最高分——处理
lst2=filter(lambda x:x<60,lst)
#调用序列操作函数和lambda表达式得到不及格数据的序列——处理
notpass=len(list(lst2))     #调用函数获得不及格人数——处理
print("最高分是{}，不及格人数是{}".format(maxscore,notpass))
#输出最高分和不及格人数——输出
