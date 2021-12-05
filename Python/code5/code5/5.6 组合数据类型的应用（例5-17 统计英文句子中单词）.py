#5.6 组合数据类型的应用（例5-17 统计英文句子中单词出现的次数）
sentence='Beautiful is better than ugly.Explicit is better than implicit.\
Simple is better than complex.Complex is better than complicated.'
#将文本中涉及标点用空格替换
for ch in ",.?!":
    sentence=sentence.replace(ch," ")
#利用字典统计词频，
# 利用split()函数拆分字符串sentence，生成单词的列表words
words=sentence.split()
map1={}  #创建一个空的字典
for word in words:   #遍历words单词列表，逐个读取列表中单词
    if word in map1:   #如果该单词已经存在于字典map1中，则次数加1
        map1[word]+=1  #其中，word作为字典的键，次数作为值
    else:              #如果该单词并未存在于字典map1中，则次数为1
        map1[word]=1
#对统计结果排序
items=list(map1.items())  #字典中的数据项转换为列表
items.sort(key=lambda x:x[1],reverse=True)  #对列表中数据项依据出现次数排序
#打印控制
for item in items:
    word,count=item
    print("{:<12}{:>5}".format(word,count))
#单词（键）左对齐打印，次数（值）右对齐打印
