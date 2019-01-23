str1='ASFDasd'
print ('D在字符串的索引是第几位：',str1.index('D'))
print ('把字符串从小写转为大写：',str1.upper())
print ('把字符串从大写转为小写：',str1.lower() )
print ('字符串是以A开头的：',str1.startswith('A') )
print ('字符串是以a开头的：',str1.startswith('a') )
print ('字符串是以S开头的：',str1.startswith('S') )
print ('字符串是以d结尾的：',str1.endswith('d') )
print ('字符串的替换：',str1.replace('asd','ASD') )
print(str1.find('F'))
print ('字符串转换成列表：',str1.split('D'))


name='tammy'
age=18
address='Xian'

print ('my name is %s,age is %s,I come from %s'%(name,age,address))
print ('my name is {0},age is {1},I come from {2}'.format(name,age,address))
print ('my name is {:s},age is {:d},I come from {:s}'.format(name,age,address))
print ('my name is {name},age is {age},I come from {address1}'.format(name=name,age=age,address1=address))


list1=[1,2,3,0,3,8,4,6,9]
print (list1.index(3))
print (list1.pop())   #默认删除最后一位并且打印
print (list1)
list1.remove(3)#默认指定要删除的元素
print (list1)
list1.reverse()   #默认反转
print (list1)


list2=['admin','tammy']
list1.extend(list2)
print (list1)
print (list2)


list2.extend(list1)
print (list1)
print (list2)
#print (help(type(list2)))


tuple=(1,2,3,4,3)
print (tuple.count(3))    #元素在元组中出现的次数
print (tuple.index(4))    #元素在元组中的索引

tuple=(1,2,3,4,3,[1,2,3],{'name':'tammy'})
#把元组中的列表由[1,2,3]修改为[1,2,3,4]
print(tuple [5])
print(tuple [5][0])
tuple[5].insert(3,4)
print(tuple [5])


#把元组中的字典name修改为weike
print (tuple[6])
tuple[6]['name']='weike'
print (tuple[6])
print(tuple)