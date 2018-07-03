'''
range详解
函数原型：range（start， end， scan):
参数含义：
start: 计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
end: 计数到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
scan： 每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
n=int(input('正方形边数'))
print('*\t'*n)
for i in range (n-2):
    print('*','\t'*(n-2),'\t*')
print('*\t'*n)


