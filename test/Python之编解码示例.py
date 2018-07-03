# -*- coding: utf-8 -*-

#decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
#encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
s = 'Python-中文'

print(s)
b = s.encode('utf-8')

print(b)
print(b.decode('utf-8'))
