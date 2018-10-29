
#多线程
import threading
import time
from threading import current_thread

def myThread(arg1,arg2):
    #获取当前线程的标志（名称、注释）
    print(current_thread().getName(),'start')
    print ('%s %s'%(arg1,arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')
for i in range(1,6,1):
    #Thread(target=传递函数名，args=传递参数)
    t1=threading.Thread(target=myThread,args=(i,i+1))
    t1.start()
print(current_thread().getName(),'end')