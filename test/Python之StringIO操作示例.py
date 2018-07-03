from io import StringIO
#StringIO经常被用来作字符串的缓存，因为StringIO的一些接口和文件操作是一致的，也就是说同样的代码，可以同时当成文件操作或者StringIO操作
# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
#getvalue返回对象中的所有数据
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    #s.readline([length])：length用于限定读取的结束位置，类型为int，缺省为None，即从当前位置读取至下一个以'\n'为结束符的当前行。读位置被移动。
    s = f.readline()
    if s == '':
        break
        #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）
    print(s.strip())
