#3.2 字符串的表示（format方法参数）
#例3-3 模板字符串与format()方法中的参数关系
#位置参数
print("{} is {} years old".format("Rose",18))
print("{0} is {1} years old".format("Rose",18))
print("Hi,{0}!{0} is {1} years old".format("Rose",18))
#关键字参数
print("{name} was born in {year},He is {age} years old".format(name="Rose",age=18,year=2000))
#下标参数
student=["Rose",18]
school=("Dalian","LNNU")
print("{1[0]} was born in {0[0]},She is {1[1]} years old".format(school,student))