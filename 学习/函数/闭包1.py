#coding:utf8
def outer(x):
    def inner(y):
        nonlocal x
        x+=y
        return x
    return inner

#inner 函数名称或函数的引用
#inner()函数的调用

a = outer(10)
print(a(1))
print(a(3))

def mulby(num):
    def gn(val):
        return num*val
    return gn

zw=mulby(7)
print(zw(9))