import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

'''
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  '''

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
'''
"form": {
    "key1": [
      "value1", 
      "value2"
    ]
    '''