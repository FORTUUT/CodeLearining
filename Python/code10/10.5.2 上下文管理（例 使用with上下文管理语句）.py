#10.5.2 上下文管理（例 使用with上下文管理语句）
fname="test.txt"
with open(fname,encoding="utf-8") as file:
  for line in file:
    print(line,end="")


