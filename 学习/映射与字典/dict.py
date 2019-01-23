#dict   代表字典，花括号，是一个hash类型，存储结构为key=vuale健值对形式，key是唯一的
#       Python3.6以下版本，字典类型无序排列，3.6以上是有序排列
if __name__ == '__main__':
    dict_module=dir(dict)
    dict_funcs=[item for item in dict_module if '__' not in item]
    print(dict_funcs)
    print(dict(a=1,b=2,c=3))
    test_dict={'c':4,'d':5,'e':6,'g':9}
    print(test_dict)
#dict.formkeys()  是从一个列表或元组中取出对应的元素，赋值给一个新的字典中的每一个key
    key=('a','b','c')
    values=(1)
    print(dict.fromkeys(key,values))
#dict.get()  输入一个key，并返回这个key对应的value，如果这个key不存在，则默认返回None，也可以传递给它一个默认值
#dict['key'] 如果这个key存在，则返回key的value，如果这个key不存在，则抛出KeyError的异常
    print(test_dict.get('f',7))
    print(test_dict['c'])
#如果需要增加或修改一个字典对应key的value，可以用dict['key']=new_value的这种方式
    test_dict['f']=7
    print(test_dict)
#dict.update()  接受一个字典，并修改字典中对应key的value
#               如果key不存在，则新增一个key并新增对应的value
    test_dict.update(f=8)
    print(test_dict)
#dict.items()   会返回一个字典对应的key,value的全部结构体，每一个元组中，存储着对应的key,value
    print(test_dict.items())
#dict.keys()    返回一个字典中全部的key，返回的结构是dict_keys类型，不能直接用index取值，如果需要用index取值
#               需要做一步转换: keys = list(dict.keys())
    print(test_dict.keys())
#dict.values()  返回一个字典中全部的value，返回的结构是dict_values类型，不能直接用index取值，如果需要用index取值
#               需要做一步转换: values = list(dict.values())
    print(test_dict.values())
#list.pop()  不需要入参，list.pop()删除的是列表中的最后一个元素，可指定删除
#dict.pop()  需要给入参 key ,dict.pop是指定key删除
    print(test_dict.pop('f'))
#dict.popitemf()  删除的是倒数第二个健值对，返回的是一个(key,value)，而pop只返回value
    print(test_dict.popitem())
#dict.setdefault  可以通过传递一个key来给字典增加一个key,value,默认的value为None
#                 如果key不存在，则新增一个key并新增对应的value，如果key存在，则不做任何修改
    test_dict.setdefault('h',10)
    print(test_dict)