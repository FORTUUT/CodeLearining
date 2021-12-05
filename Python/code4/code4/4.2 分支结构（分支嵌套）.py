#4.2 分支结构（分支嵌套）
score=eval(input("请输入成绩："))
if(score>=80):
    if(score>=90):
        print("成绩优秀。")
    else:
        print("成绩良好。")
else:
    if(score>=60):
        print("成绩合格。")
    else:
        print("成绩不合格。")
