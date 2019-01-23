dict1={'name':'tammy','age':18,'address':'hangzhou'}

#获取到字典中key对应的具体value值
print(dict1['age'])
print(dict1.get('age'))

#获取到所有的KEY值
for key in dict1.keys():
	print (key)
#获取到所有的value值
for value in dict1.values():
	print(value)

#对字典循环
for key,value in dict1.items():
	print(key,':',value)
list1=['admin','ADMIN']
print('1'.join(list1))



list1=[1,2,3,4,5]
tuple1=tuple(list1)
print (tuple1)

list2=list(tuple1)
print(list2)

dict1={'name':'tammy','age':18,'adress':'hangzhou'}
list3=dict1.items()
print(list3, type(list3))

a = {'a': 1, 'b': 2, 'c': 3}

# 字典中的key转换为列表
key_value = list(a.keys())
print('字典中的key转换为列表：', key_value)

# 字典中的value转换为列表
value_list = list(a.values())
print('字典中的value转换为列表：', value_list)

list1=[1,2,3,4,5]
dict2=dict(enumerate(list1))
print(dict2,type(dict2))