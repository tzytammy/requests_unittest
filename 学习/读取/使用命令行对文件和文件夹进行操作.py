import os
#根据相对路径的.来获取当前绝对路径
print(os.path.abspath('.'))
#根据相对路径的.来获取当前绝对路径的上一级路径
print(os.path.abspath('..'))
#判断是否存在某一路径
print(os.path.exists('/user'))
#判断是否是文件、是否是文件夹
print(os.path.isfile('/user'))
print(os.path.isdir('/user'))

from pathlib import  Path
#根据相对路径的.来获取当前绝对路径
#封装
p=Path('/tmp/a/b/c')
print(p.resolve())

print(p.is_dir())
#新建
q=Path('/tmp/a/b/c')
Path.mkdir(q,parents=True)