
#!/usr/bin/python
# -*- coding: utf-8 -*-

li = [1,2,3,4,5,6,7,8,9]
print ([x**2 for x in li])

print ([x**2 for x in li if x>5])

print (dict([(x,x*10) for x in li]))

print  ([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8 ])

vec=[2,4,6]
vec2=[4,3,-9]
sq = [vec[i]+vec2[i] for i in range(len(vec))]
print (sq)

print ([x*y for x in [1,2,3] for y in  [1,2,3]])

testList = [1,2,3,4]
def mul2(x):
    return x*2
print ([mul2(i) for i in testList])

#过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
names = ['bob','tom','alice','jerry','wendy','smith']
print([name.upper() for name in names if len(name)>3])
#['ALICE', 'JERRY', 'WENDY', 'SMITH']


#求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表

print([(x,y) for x in range (6) if x%2==0 for y in range(6) if y%2])


#求m中3,6,9组成的列表
m=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print([m[row][2] for row in (0,1,2)])
print([m[i][i] for i in range(len(m))])



bob={'pay': 3000, 'job': 'dev', 'age': 42, 'name': 'bob smith'}
sue={'pay': 4000, 'job': 'hdw', 'age': 45, 'name': 'sue jones'}
people = [bob, sue]
print([rec['age']+100 if rec['age'] >= 45 else rec['age'] for rec in people] )# 注意for位置

#如下的列表推导式结合两个列表的元素，如果元素之间不相等的话:

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
