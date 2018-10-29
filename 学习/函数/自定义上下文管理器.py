

fd=open('name.txt',encoding='utf-8')
try:
    for line in fd:
            print(line)
finally:
    fd.close()


#上下文管理器
'''正常情况下，你要显示的打开和关闭文件。但如果你用with语句，就会更可读，且永远不会因为忘记关闭文件而担忧：'''
with open('name.txt',encoding='utf-8') as f:
    for line in f:
        print(line)