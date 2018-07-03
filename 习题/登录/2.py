name= "seven"
password='123'
inputname=input("请输入用户姓名：")
inputpw=str(input("请输入用户密码："))


if inputname==name and inputpw==password:
    print("登录成功！")
else:
    print("登录失败，请重新登录")
