import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
#获取title
print(soup.title)

#获取a标签
tag=soup.a
#获得标签的名字
print(soup.a.name)
#获取标签的属性信息
print(tag.attrs)
#提取字典中某个属性
print(tag.attrs['class'])
#获取a标签的链接属性
print(tag.attrs['href'])
#查看标签属性的类型
print(type(tag.attrs))

print(type(tag))
print(tag)
print(tag.string)
print('-----------------------------------')
print(soup.p)
print(soup.p.string)


print('-------------new--------------------')
newsoup=BeautifulSoup("<b><!--This is a comment --></b><p>This is not a comment</p>","html.parser")
print('newsoup:')
print(newsoup)
print('newsoup.b:')
print(newsoup.b)
print('newsoup.b.string:')
print(newsoup.b.string)
print('type(newsoup.b.string):')
print(type(newsoup.b.string))

print('newsoup.p.string:')
print(newsoup.p.string)
print('type(newsoup.p.string):')
print(type(newsoup.p.string))
