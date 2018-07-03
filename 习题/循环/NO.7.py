'''
使用 while 循环实现输出 1-100 内的所有奇数
'''

i=0
while i<100:
    i=i+1
    if i%2==0:
        continue
    else:
        print("奇数",i)