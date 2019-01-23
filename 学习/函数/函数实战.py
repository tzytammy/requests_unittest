
'''
1、模拟登陆
2、模拟登陆成功显示登陆成功后的用户账号
3、模拟注册
'''

def regetist(username,password):
	'''

	:param username: 注册系统的账号
	:param password: 注册系统的密码
	:return:
	'''

	temp=username+'|'+password
	f=open('login','w',encoding='utf-8')
	f.write(temp)



def login(username,password):
	'''
	登录
	:param username: 登录系统账号
	:param password: 登录系统密码
	:return:
	'''

	f=open('login','r')
	for line in f:
		#把字符串转成列表
		list=line.split('|')

		if list[0]==username and list[1]==password:
			print('恭喜您登录成功')
			return True
		else:
			print('很遗憾，登录失败')
			return  False





def info():
	'''
	系统登录后的用户信息页面
	:return:
	'''
	f=open('login','r')
	for line in f:
		#把字符串转为list
		list=line.split('|')
	r=login()
	if r:

		print ('登录成功，用户昵称：{0}'.format(list[0]))
	else:
		print('登录失败')

def main():
	'''
	主函数
	:return:
	'''
	while True:
		t=int(input('请输入数字：1、注册 2、登录 3、查看用户信息\n'))
		if t==1:
			username = input(u'请输入注册的账号：\n')
			password = input(u'请输入注册的密码：\n')
			regetist(username,password)
		elif t==2:
			username = input(u'请输入你登录的账号：\n')
			password = input(u'请输入你登录的密码：\n')
			login(username,password)
		elif t==3:
			info()
		else:
			print('请继续输入')
main()