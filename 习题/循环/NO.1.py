'''
使用 while 循环实现输出 2-3+4­-5+6 ...+100 的和
'''

i=1
count=0
while i<100:
    i=i+1
    if i%2==0:
        count=count+i
    else:
        count=count-i
print (count)