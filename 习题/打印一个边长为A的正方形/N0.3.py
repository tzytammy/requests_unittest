
#空心正方形
rows=int(input('正方形边数'))
for i in range(rows):
    if (i == 0) | (i == rows-1):
        for j in range(rows):
            print('*\t', end='')
    else:
        for j in range(1):
            print('*\t', end='')

        for j in range(rows-2):
            print('\t', end='')
        for j in range(1):
            print('*', end='')
    print()

