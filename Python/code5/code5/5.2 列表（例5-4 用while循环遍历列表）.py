#5.2 列表（例5-4 用while循环遍历列表）
lst=list(range(2,21,3));print(lst)
i=0;result=[]
while i<len(lst):
    result.append(lst[i]*lst[i])
    i+=1
print(result)