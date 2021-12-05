#9.2 文件的打开与关闭（例9-1 以各种模式打开文件）
#默认以只读方式打开，文件不存在时报异常
#file1=open("readme.txt")
#以只读方式打开
file2=open("s1.py",'r')
print(file2.read())
#以读/写方式打开二进制文件
file3=open("G:\\2021-2022-1\\Python\\PPT\\ch9\code9\\test.txt",'w+')
file3.write("Hello Python!\n"
            "Python提供了一组读取文件内容的方法。对于当前文件下文本文件myfile.py\n"
            "本文件是文本文件，默认编码格式ANSI\n")
file3.close()
file3=open("G:\\2021-2022-1\\Python\\PPT\\ch9\code9\\test.txt",'r')
print(file3.read())
#以读/写方式打开二进制文件,如果不存在，则创建新文件用于读写
file4=open("picture.jpg","ab+")
print(file4.read())
#file4.seek(0)
#print(file4.read())





