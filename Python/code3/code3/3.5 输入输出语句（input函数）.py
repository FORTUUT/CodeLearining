#3.5 输入输出语句（input函数）
#例3-12 使用input()函数输入数据
name=input("请输入姓名：")
print(name)
score1=eval(input("请输入科目1成绩："))
score2=eval(input("请输入科目2成绩："))
print("科目1+科目2的总成绩是：",score1+score2)
score3=int(input("请输入科目3成绩（整数）："))
score4=float(input("请输入科目4成绩（实数）："))
print("科目3+科目4您的总成绩是：",score3+score4)