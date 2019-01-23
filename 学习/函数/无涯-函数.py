def f4(name,age,sex,**kwargs):
	print (u'用户信息：',name,age,sex,kwargs)

f4('tammy',18,'girl')
f4('tammy',18,'girl',code='32324234324324',phone='13654447777',adress='HK')


def f2(*args):
	print (args,type(args))

def f3(**kwargs):
	print (kwargs,type(kwargs))

f2()
f3()

def f5(*args,**kwargs):
	print (args,kwargs)

f5()
f5(2)
f5(adress='xian')