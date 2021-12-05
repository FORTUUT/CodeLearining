#8.6.1 jieba库简介（英文句子中单词拆分到列表）
str1="the Zen of Python"
print(str1.split())

import jieba
str2="Python是一种优美简洁的计算机程序设计语言"
print(str2.split())
print(jieba.lcut(str1))
print(jieba.lcut(str2))

