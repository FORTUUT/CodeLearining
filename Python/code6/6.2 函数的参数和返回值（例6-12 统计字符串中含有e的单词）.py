#6.2 函数的参数和返回值（例6-12 统计字符串中含有'e'的单词）.py
def findwords(sentence):
    "统计参数中含有字符e的单词，保存到列表中，并返回"
    result=[]
    words=sentence.split()
    for word in words:
        if word.find("e")!=-1:
            result.append(word)
    return result

ss="Return the lowest index in S where substring sub is found,"
print(findwords(ss))

