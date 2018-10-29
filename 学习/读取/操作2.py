file = open("name1.txt",encoding="utf-8")
print(file.read())

file1 = open("name1.txt",encoding="utf-8")
print(file1.readline())

file2=open("name1.txt",encoding="utf-8")
for line in file2.readlines():
    print(line)
    print("=======")

#回到文件开头再次操作
file6=open('name1.txt',encoding="utf-8")
print(file6.tell())  #指针记录当前位置
file6.read(1)
print(file6.tell())

#操纵指针
file6.seek(7)
print(file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))

#?问题：为什么中文不行？
file6 = open('name1.txt',encoding='utf-8')
print('当前文件指针的位置 %s' %file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
# 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移，   2 从文件结尾
file6.seek(5,0)
print('我们进行了seek操作')
print('当前文件指针的位置 %s' %file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
file6.close()
