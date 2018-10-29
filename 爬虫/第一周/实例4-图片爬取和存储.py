import requests
import os
path='E:/abc.jpg'
url='https://edu-image.nosdn.127.net/DB7993B072C5E5E6A5C13D31BD3D8A0F.jpg?imageView&thumbnail=510y288&quality=100'

r=requests.get(url)
print(r.status_code)

#保存文件
with open(path,'wb') as f:
    f.write(r.content)