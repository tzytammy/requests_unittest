# -*- coding: utf-8 -*-

import json

# 从字典构建json串
d = dict(name='Bob', age=20, score=88)
# json.dumps()用于将dict类型的数据转成str
# 因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。
data = json.dumps(d)
print('JSON Data is a str:', data)

# 载入json字符串
# json.loads()用于将str类型的数据转成dict
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)