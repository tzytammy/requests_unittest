rows=int(input('正方形边数：'))
i=0
while i<=(rows-1):
    if i==0 or i==(rows-1):
        print ('*\t'*rows)
    else:
        print('*'+'\t'*(rows-1)+'*')
        #print('*', '\t' * (rows- 2), '\t*')
    i+=1