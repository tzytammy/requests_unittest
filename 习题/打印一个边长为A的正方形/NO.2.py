
#实心正方形
'''
print()，在输出中自动包含换行”的默认行为。
print("\t",end='');
其原理是：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。
'''
rows=int(input('正方形边数'))
for i in range(rows):
    for j in range(rows):
        print(' \t*', end='')
    print()

'''
for i in range(rows):
    print(' \t*', end='')
'''

