name=['seven','alex']
password=123
count=0
for count in  range(0,3):
    inputname = input("请输入用户姓名：")
    inputpw = int(input("请输入用户密码："))
    if inputname in name and inputpw== password:
        print("登录成功！")
        break
    else:
        print("登录失败，请重新登录")
        count=count+1
        if count==3:
            print ("登录失败超过三次，无法再次输入")
         