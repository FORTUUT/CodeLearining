#8.6.3 添加单词和自定义词典（例8-14 向分词库添加单词）.py
import jieba
print(jieba.lcut("斯凯温是一个优秀的外语教师"))
print(jieba.lcut("黄土窑的未来值得人们向往"))
jieba.add_word("黄土窑")
print(jieba.lcut("黄土窑的未来值得人们向往"))

