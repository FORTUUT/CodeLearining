#3.4 字符串处理函数（字符串判断）
#例3-8 字符串判断函数的应用
#是否都是字母或数字，因为存在$,返回False
print("aabbcc$123".isalnum())
#是否都是字母，False
print("hello9".isalpha())
#是否只包含数字，True
print("123".isdigit())
#是否只包含数字字符，识别全角数字，True
print("123".isnumeric())
#是否只包含数字字符，识别汉字数字，True
print("12二".isnumeric())
#是否只包含数字，不识别汉字是数字，False
print("12二".isdigit())
#是否包含都是大写字符，False
print("ABc".isupper())