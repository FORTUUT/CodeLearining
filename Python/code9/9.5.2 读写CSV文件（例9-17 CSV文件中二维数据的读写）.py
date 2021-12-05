# 9.5.2 读写CSV文件（例9-17 CSV文件中二维数据的读写）.py
# 使用内置csv模块写入和读取二维数据
datas = [['Name', 'DEP', 'Eng','Math', 'Chinese'],
['Rose', '法学', 89, 78, 65],
['Mike', '历史', 56,'', 44],
['John', '数学', 45, 65, 67]
]





import csv
filename = 'bsheet.csv'
#先执行with后面的函数open，返回值赋给as后面的变量f
with open(filename, 'w',newline="") as f:
    writer = csv.writer(f)   #获得写入器
    for row in datas:        #遍历二维列表datas的每一个元素（一维列表）
        writer.writerow(row)     #写入器调用行写入方法写入每一行（对应一维列表）
ls=[]
with open(filename,'r') as f:
    reader = csv.reader(f)    #获得读取器
    #print(reader)
    for row in reader:        #通过读取器，获取CSV的每一行
        print(reader.line_num, row)    # 行号从1开始，行号+CSV每行数据
        ls.append(row)        #放入列表以便显示
    print(ls)
        



