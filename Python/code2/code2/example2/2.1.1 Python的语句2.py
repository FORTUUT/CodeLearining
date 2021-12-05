#2.1.1 Python的语句2
'''
a=1;b=2;c=3;   #一行内多条语句分号分隔
print(a);print(b);print(c)  #一行内多条语句分号分隔
print(a+10)
print(b+10)
print(c+10)   #建议每行一条语句，结束不写分号
'''

#一条语句过长，需要换行书写，语句外部加上一对圆括号实现
str1=("当一条语句过长时，可能需要进行换行处理，这时可以\
在语句的外侧加上一对圆括号来实现。也可以使用\
反斜杠来分行书写。")        #第1种写法，用\续行
str2=("当一条语句过长时，可能需要进行换行处理，这时可以"
      "在语句的外侧加上一对圆括号来实现。"
      "也可以使用反斜杠来分行书写。")  #第2种写法
print(str1)
print(str2)
#写在[]和{}内的跨行语句视为一行语句，不需要圆括号换行
months=['january','febrary','march','april',
        'may','june','july','august','september',
        'october','november','december']
week={'Monday','Tuesday','Wednesday','Thursday',
      'Friday','Saturday','Sunday'}
print(months)
print(week)