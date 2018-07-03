# -*- coding: utf-8 -*-

from datetime import datetime

# 写模式
with open('test.txt', 'w',encoding='utf-8') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

# 读模式
with open('test.txt', 'r',encoding='utf-8') as f:
    s = f.read()
    print('open for read...')
    print(s)

# 二进制读模式
with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

