import requests
url='https://www.amazon.cn/gp/product/B01M8L5Z3Y'

try:
    # 模仿浏览器登录访问
    kv = {'user-agent': 'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    #截取从1开始到999个字符
    print(r.text[:1000])
    print(r.request.headers)
except:
    print("error")
    print(r.request.headers)

