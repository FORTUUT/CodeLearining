#6.5 Python的内置函数（例6-28 filter()函数的应用）
#filter()函数第一个参数是lambda函数，筛选奇数
f1=filter(lambda x:x%2,[1,2,3,4,5])
print(list(f1))
#filter()函数第一个参数是vowel()函数，筛选含有元音字符的单词
def vowel(word):
    if word.find('a')>=0 or word.find('e')>=0 or word.find('i')>=0\
        or word.find('o')>=0 or word.find('u')>=0:
        return word
f2=filter(vowel,["python","php","java","c++","html"])
print(list(f2))