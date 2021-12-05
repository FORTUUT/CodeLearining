#8.6.1 添加单词和自定义词典（例8-15 用户自定义词典的应用）.py
import jieba
print(jieba.lcut("张林一是创新办主任也是云计算方面的专家"))
print(jieba.load_userdict('dict1.txt'))
print(jieba.lcut("张林一是创新办主任也是云计算方面的专家"))
print('/'.join(jieba.cut('如果放到post中将出错。')))
print(jieba.suggest_freq(('中','将'),True))
print('/'.join(jieba.cut('如果放到post中将出错。',HMM=False)))