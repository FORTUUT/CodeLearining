# 9.5.2 读写CSV文件（例9-18 处理CSV文件的数据，显示整洁的二维数据）.py
# 使用内置csv模块写入和读取二维数据
datas = [['Name', 'DEP', 'Eng','Math', 'Chinese'],
['Rose', '法学', 89, 78, 65],
['Mike', '历史', 56,'', 44],
['John', '数学', 45, 65, 67]
]
import csv
filename = 'bsheet.csv'
str1=''
with open(filename,'r') as f:
    reader = csv.reader(f)
    #print(reader)
    for row in reader:
        for item in row:
            str1+=item+' '
        str1+='\n'
        print(reader.line_num, row)    # 行号从1开始
    print(str1)    



