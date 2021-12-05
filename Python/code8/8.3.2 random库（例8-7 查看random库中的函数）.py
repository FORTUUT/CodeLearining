#8.3.2 random库（例8-7 查看random库中的函数）
import random
print(dir(random))
print(random.random()," ",random.randint(10,20)," ",random.randrange(10))
print(random.choice(['a','b','c','d','e'])," ",random.uniform(10,20))
print(random.randrange(1,20,3))
lst=['a','b','c','d','e']
random.shuffle(lst)   #随机打乱可变序列的元素顺序
print(lst)
random.seed(a=None)  #不设置初始值，系统根据时间选择，每次生成随机数序列因时间差异而不同。
for i in range(3):print(random.random())
random.seed(9)   #设置初始值，随机数生成函数每次生成的随机数序列都相同。
for i in range(3):print(random.random())

