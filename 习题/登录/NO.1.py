'''
https://www.cnblogs.com/yangjian1/p/6061057.html
实现用户输入用户名和密码，当用户名为seven且密码为123时，
显示登陆成功，否则登陆失败！
'''

name='seven'
password=123
inputname=input("请输入用户姓名：")
inputpw=int(input("请输入用户密码："))

if inputname==name:
    if inputpw==password:
        print("登录成功")
    else:
        print("登录失败")
else:
    print("登录失败")


'''if inputname==name and inputpw==password:
    print("登录成功！")
else:
    print("登录失败，请重新登录")'''

