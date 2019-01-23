'''
 编写一个从 1 加到 end 的当型循环。变量 end 的值由键盘输入。假如输入 end
的值为 6，则代码输出的结果应该是 21，也就是 1+2+3+4+5+6 的结果（不要用
sum 作为变量，因为它是内置函数）。
'''

s=int(input('请输入end数字:'))
sum=0
for i in range(s+1):
    sum=sum+i
print(sum)