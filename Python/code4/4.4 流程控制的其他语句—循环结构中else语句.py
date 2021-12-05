#4.4 流程控制的其他语句—循环结构中else语句
#例4-13 在循环结构中使用else语句示例。
str1="Hi,Python"
for ch in str1:
    print(ch,end="")
    if(ch=='P'):break
else:
    print("字符串遍历结束")