
#将小说的主要人物记录在文件中
'''w：以只写模式打开文件，并将文件指向指针指向文件头
如果文件存在则将其内容清空
如果文件不存在则创建
'''
file1=open('name.txt','w',encoding="utf-8")

file1.write('诸葛亮')

file1.close()

file2=open('name.txt',encoding="utf-8")
print(file2.read())
file2.close()

file3=open('name.txt','a',encoding="utf-8")
file3.write('哈哈')
file3.close()

file4=open('name.txt',encoding="utf-8")
print(file4.read())
file4.close()
