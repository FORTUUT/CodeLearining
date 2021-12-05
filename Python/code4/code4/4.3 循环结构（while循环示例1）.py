#4.3 循环结构（while循环示例1）
#将一个列表中的元素进行头尾置换并输出
lst = [1,3,7,-23,34,0,23,2,9,7,79]

head = 0
tail = len(lst)- 1
while head <len(lst)/2 :
    lst[head],lst[tail]=lst[tail],lst[head] #头尾互换
    head+=1   #调整头指针后移
    tail-=1   #调整尾指针前移

for item in lst:
    print(item,end="  ")
