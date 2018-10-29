#并行生产，并行消费
from threading import Thread,current_thread
import time
import random
from queue import Queue
#只可以容纳5个数字
queue = Queue(5)

class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' %(name, num))
            t = random.randint(1,3)   #经过随机时间往队列中填加数字
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' %(name, t))

class ConsumerTheard(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            #封装了线程等待
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' %(name, num))
            t = random.randint(1,5) #经过随机时间从队列中提取数字
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


p1 = ProducerThread(name = 'p1')
p1.start()
p2 = ProducerThread(name = 'p2')
p2.start()
p3 = ProducerThread(name = 'p3')
p3.start()
c1 = ConsumerTheard(name = 'c1')
c1.start()
c2 = ConsumerTheard(name = 'c2')
c2.start()