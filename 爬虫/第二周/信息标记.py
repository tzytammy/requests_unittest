'''
实例：提取HTML中所有URL链接
1)搜索到所有<a>标签
2)解析<a>标签格式，提取href后的链接内容
'''

import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print (soup)
for link in soup.find_all('a'):
    print(link.get('href'))

print('===============内容查找方法======================')
print(soup.find_all('a'))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(soup.find_all(['a','b']))
for tag in soup.find_all(True):
    print (tag.name)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#只显示b标签/body标签
import re
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(soup.find_all(id='link1'))