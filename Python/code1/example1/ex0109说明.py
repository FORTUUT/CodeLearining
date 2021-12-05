# program0109.py
file=open("file.txt",'r') #只读打开文件——输入
s1=file.read()            #读字符串——输入
file.close()              #关闭文件——输入
lst=s1.split(',')         #字符串拆分获取数据列表1——处理
lst2=[]                   #创建列表2——处理
for item in lst:          #for循环获取列表1中数据项——处理
    lst2.append(eval(item))  #列表1中数据项放入列表2——处理
#print(lst2)
#notpass为不及格人数，maxscore为最高分
notpass =maxscore= 0   #初始化变量——处理
for item in lst2:      #for循环获取列表2中数据项——处理
    if maxscore<item:  #分析判断数据项——处理
        maxscore=item  #赋值获取最高分——处理
    if item<60:        #分析判断数据项——处理
        notpass+=1     #统计不及格人数——处理
print("最高分是{}，不及格人数是{}".format(maxscore,notpass))

