# -*- coding: utf-8 -*-

# 定义几个类
class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

# 初始化不同的类对象
a = Animal()
d = Dog()
h = Husky()

# 判断类对象的类型
print('check a = Animal()...')
print('isinstance(a, Animal) =', isinstance(a, Animal))
print('isinstance(a, Dog) =', isinstance(a, Dog))
print('isinstance(a, Husky) =', isinstance(a, Husky))

print('check d = Dog()...')
print('isinstance(d, Animal) =', isinstance(d, Animal))
print('isinstance(d, Dog) =', isinstance(d, Dog))
print('isinstance(d, Husky) =', isinstance(d, Husky))

print('check h = Husky()...')
print('isinstance(h, Animal) =', isinstance(h, Animal))
print('isinstance(h, Dog) =', isinstance(h, Dog))
print('isinstance(h, Husky) =', isinstance(h, Husky))