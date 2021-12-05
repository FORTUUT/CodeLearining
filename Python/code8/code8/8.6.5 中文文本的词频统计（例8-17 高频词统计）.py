# 8.6.5 中文文本的词频统计（例8-17 高频词统计）.py
'''
使用jieba库分解中文文本，并使用字典实现词频统计
'''
# encoding=utf-8
import jieba
# read need analyse file
article = open("sanguo60.txt",encoding='utf-8').read()
#article = open("shuihu70.txt",encoding='utf-8').read()
words = jieba.lcut(article)
#  count word freq
word_freq = {}
for word in words:
    if len(word)==1:
        continue
    else:
        word_freq[word]= word_freq.get(word,0)+1
        #如果单词存在则返回值，否则返回0，加1后，词频为1，否则返回值词频加1
#  sorted    
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x:x[1], reverse=True)
max_number = eval(input("显示前多少位高频词？ "))
# display
for word, freq in freq_word[:max_number]:
    print(word, freq)
