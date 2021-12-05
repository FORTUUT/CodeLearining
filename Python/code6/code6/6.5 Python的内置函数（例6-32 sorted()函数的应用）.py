#6.5 Python的内置函数（例6-32 sorted()函数的应用）
str1=['a','b','d','c','B','A']
#默认按字符的ASCII码排序
print(sorted(str1))
#转换成小写字母后再排序
print(sorted(str1,key=str.lower))
print(sorted(str1,reverse=True,key=str.lower))