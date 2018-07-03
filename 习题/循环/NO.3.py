'''
使用 for 循环和 range 实现输出1-2+3-4+5-6....-98+99  的和
'''

count=0
for i in range(1,100):
    if i%2==0:
        count=count-i
    else:
        count=count+i
print('1-2+3-4+5-6....-98+99  的和',count)