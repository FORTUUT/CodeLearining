#8.1.4 模块搜索路径
import sys
print(sys.path)
#搜索路径：
# （1）程序当前目录
# （2）操作系统环境变量pythonpath包含的目录(如果存在)
# （3）Python标准库目录
# （4）任何.pth文件包含的目录(如果存在)
import os
print(os.getcwd())  #程序的当前目录