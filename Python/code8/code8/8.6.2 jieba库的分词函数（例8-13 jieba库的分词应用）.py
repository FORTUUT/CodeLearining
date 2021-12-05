#8.6.2 jieba库的分词函数（例8-13 jieba库的分词应用）
import jieba
str3="Python是一种优美简洁的计算机程序设计语言"
seg_list=jieba.cut(str3)
print(seg_list)
for s in seg_list:print(s,end=',')
print(s)
print(jieba.lcut(str3))
print(jieba.lcut(str3,cut_all=True))
print(jieba.lcut_for_search(str3))