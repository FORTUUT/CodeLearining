#3.4 字符串处理函数（拆分合并）
#例3-11 字符串拆分与合并函数的应用
str1="hi,Python,hi,Java!"
#默认使用空格做分配符，str1中无空格，
# 列表中只有一个元素
print(str1.split())
#使用逗号做通配符，3个逗号，分隔3次
print(str1.split(","))
#使用逗号做分配符，限制分隔2次
print(str1.split(",",2))
lst=['hi','Python!','hi','Java!']
#将列表连接为字符串
s=""; print(s.join(lst))
