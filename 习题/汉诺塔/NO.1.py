def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move (n-1,a,c,b)#将A柱第n个盘子上面的n-1个盘子借助C柱虚拟移到B柱，此时，这n-1个盘子已经在B柱上
        print (a,'->',c)
        move(n-1,b,a,c)
number=int(input("请输入盘子数："))
move (number,'A','B','C')
