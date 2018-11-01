import requests
url='https://www.baidu.com'
kv={'wd':'python'}
try:
    r=requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    #截取从1开始到999个字符
    print(r.text[:1000])
    print(r.request.url)
except:
    print("error")

