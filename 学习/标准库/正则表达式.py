import re

#定义一个要匹配的正则表达式
# p=re.compile('ca*t')
#
# #需要匹配的字符串
# print(p.match('caaaaaaaaat'))

#
# p=re.compile('c..t.jpg$')
#
# #需要匹配的字符串
# print(p.match('cawt.jpg'))


p=re.compile(r'(\d+)-(\d+)-(\d+)')

#需要匹配的字符串
# print(p.match('2018-09-25'))
# print(p.match('2018-09-25').group(3))
# year,month,day=p.match('2018-09-25').groups()
# print(year)
# print(r'\nx\n')

print (p.search('aa2018-05-10bb'))
phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*$','',phone)
print(p2)
p3 = re.sub(r'\D','',p2)
print(p3)
