import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,'html.parser')


#下行遍历
print("soup.head:",soup.head)
print("soup.head.contents:",soup.head.contents)
print("soup.body.contents:",soup.body.contents)
print(len(soup.body.contents))
print('NO.1：',soup.body.contents[1])

for child in soup.body.children:
    print(child)

print('--------------------')
for child in soup.body.children:
    print(child)


#上行遍历

print('-------------上行遍历-------------')
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


#平行遍历

print('-------------平行遍历-------------')
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling.previous_sibling)

print('----------遍历后续节点-------------')
for sibling in soup.a.next_sibling:
    print(sibling)

print('--------遍历前续节点---------------')
for sibling in soup.a.previous_sibling:
    print(sibling)


