#单线程
def myThread(arg1,arg2):
    print ('%s %s'%(arg1,arg2))
for i in range(1,6,1):
    t1=myThread(i,i+1)

