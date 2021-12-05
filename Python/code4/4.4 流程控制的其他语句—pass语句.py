#4.4 流程控制的其他语句—pass语句
#例4-12 pass语句示例。打印列表中的奇数。
for i in [1,4,7,8,9]:
    if i%2==0:
        pass
        print("pass语句处将来可添加偶数处理代码")
        continue
    print("奇数",i)
