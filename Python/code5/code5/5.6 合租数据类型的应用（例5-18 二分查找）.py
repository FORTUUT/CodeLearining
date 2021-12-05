#5.6 合租数据类型的应用（例5-18 使用二分查找）
list1 = [1,42,3,-7,8,9,-10,5]
#二分查找要求查找的序列时有序的，假设是升序列表
list1.sort(); print(list1)
find=eval(input("请输入要查看的数据："))
#low和high作为列表下标，用来查找元素，相当于指针作用
#low和high的增减，相当于指针的移动
low = 0; high = len(list1)-1; flag=False
while low <= high :    #当low指针小于high指针时
    mid = int((low + high) / 2)
    if list1[mid] == find: #找到指定的数据，则退出
        flag=True
        break
    #左半边  #左半边查找比较，high指针左移
    elif list1[mid] > find:
        high = mid -1
    #右半边  #右半边查找比较，low指针右移
    else :
        low = mid + 1


if flag==True:
    print("您查找的数据{},是第{}个元素".format(find,mid+1))
else:
    print("没有您要查找的数据")
