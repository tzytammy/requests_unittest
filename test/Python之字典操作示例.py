# -*- coding: utf-8 -*-

# 定义并初始化字典
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
# 获取字典值的姿势
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])

#dict.get(key, default=None)
#key -- 字典中要查找的键。
#default -- 如果指定键的值不存在时，返回该默认值值。

print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
