#8.6.4 基于TF-IDF算法的关键词抽取（例8-16 基于TF-IDF算法的关键词抽取的示例）.py
#TF-IDF（term frequency–inverse document frequency）是一种用于信息检索与数据挖掘的常用加权技术。
# TF是词频(Term Frequency)，
# IDF是逆文本频率指数(Inverse Document Frequency)。
import jieba.analyse
import jieba
content='''用户可以指定自己自定义的词典，以便包含jieba词库里没有的词。
虽然jieba有新词识别能力，但是自行添加新词可以保证更高的正确率。
jieba.load_userdict(file_name)方法用于添加字典，
其中，file_name为文件类对象或自定义词典的路径'''
tags=jieba.analyse.extract_tags(content,topK=5)
print(tags)