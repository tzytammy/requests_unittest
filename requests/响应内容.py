import requests

r = requests.get('https://api.github.com/events')
print(r.text)
print(r.encoding)
#响应状态码
print(r.status_code)

print(r.status_code == requests.codes.ok)
#抛出异常
print(r.raise_for_status())

#JSON响应内容
r = requests.get('https://api.github.com/events')
print(r.json())

