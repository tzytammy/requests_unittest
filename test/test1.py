# -*- coding: utf-8 -*-
print('1024*768 =', 1024*768)

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)
n = 123
f = 456.789

s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print('s1=','hello,wprlg')
print('s2=','Hello,\\\'Adam\\\'')

print(str('\u4e2d\u6587'))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
