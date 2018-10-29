class Testwith():
    #对类进行初始化
    def __enter__(self):
        print('run')
    #对类进行结束
    #exc_tb 判断异常
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has error %s'%exc_tb)


with Testwith():
    print('test is runing')
    raise  NameError('test Nameerror')