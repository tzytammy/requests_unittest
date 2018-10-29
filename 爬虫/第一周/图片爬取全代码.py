import requests
import os

url='https://edu-image.nosdn.127.net/DB7993B072C5E5E6A5C13D31BD3D8A0F.jpg'
root='E://123'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        print (path)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
