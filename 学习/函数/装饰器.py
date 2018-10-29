import time

# def ican_sleep():
#     time.sleep(3)
# start_time=time.time()
# ican_sleep()
# stop_time=time.time()
# print('time is',stop_time-start_time)

def timmer(func):
    def wrapper():
        start_time=time.time()
        func()
        stop_time = time.time()
        print('time is %s 秒' %(stop_time - start_time))
    return wrapper

@timmer
#timer装饰函数，修饰下面 i_can_sleep 被装饰函数
def i_can_sleep():
    time.sleep(3)

i_can_sleep()
#timer(i_can_sleep() )