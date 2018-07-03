# -*- coding: utf-8 -*-

# 动物基类
class Animal(object):
    def run(self):
        print('Animal is running...')

# 单身狗类
class Dog(Animal):
    def run(self):
        print('Dog is running...')

# 可爱猫类
class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 跑两次
def run_twice(animal):
    animal.run()
    animal.run()

# 初始化
a = Animal()
d = Dog()
c = Cat()

# 打印类型
'''
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
'''
d.run()
a.run()
c.run()
print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Animal?', type(d)== Animal)
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))