# program0107.py
lst=[89,45,-34,23.1,98,33]  #——列表数据赋值输入
#notpass为不及格人数，maxscore为最高分
notpass =maxscore= 0   #初始化变量——处理
for item in lst:       #利用for循环求列表中数据项——处理
    if maxscore<item:  #判断分析——处理
        maxscore=item   #赋值最大值——处理
    if item<60:        #判断分析——处理
        notpass+=1      #统计不及格人数——处理
print("最高分是{}，不及格人数是{}".format(maxscore,notpass))
#输出最高分和不及格人数——输出
