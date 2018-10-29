#变量没有被定义
#i = j

#语法错误
#print())

# a='123'
# print(a[3])


# d={'a':1,'b':2}
# print(d['c'])



# year=int (input("input year"))

# try:
#     year=year=int (input("input year"))
# except ValueError:
#     print("年份要输入数字")
#
# a=123
# a.append()


# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print("o不能作为除数 %s",e)

'''
except可以处理一个专门的异常，如果except后没有指定异常，则默认处理所有的异常。每一个try，都必须至少有一个except
# '''
# try:
#     #使用raise抛出异常，一旦执行了raise语句，raise后面的语句将不能执行。
#     raise NameError("hello world")
#     #自定义错误信息
# except NameError:
#     print('my custom error')


try:
    a=open('name.txt')
except Exception as e:
    print(e)

finally:
    a.close()

