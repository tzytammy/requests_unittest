#读取人物名称
f=open('name.txt',encoding='utf-8')
data=f.read()
print(data.split("|"))

#读取兵器名称
f2=open('weapon.txt',encoding='utf-8')
#data2=f2.read()
i=1
for line in f2.readlines():
    if i%2==1:
        print (line.strip('\n'))
        #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    i +=1

f3=open('sanguo.txt',encoding='utf-8')
print(f3.read().replace('\n',''))

