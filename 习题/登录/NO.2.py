'''
实现用户输入用户名和密码，当用户名为 seven且密码为 123 时，
显示登陆成功，否则登陆失败，失败时允许重复输入三次
'''

name='seven'
password=123
count=0
for count in  range(0,3):
    inputname = input("请输入用户姓名：")
    inputpw = int(input("请输入用户密码："))
    if inputname==name and inputpw== password:
        print("登录成功！")
        break
    else:
        print("登录失败，请重新登录")
        count=count+1
        print (count)
        if count==3:
            print ("登录失败超过三次，无法再次输入")