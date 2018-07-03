'''
使用 while 循环实现输出 2-3+4­-5+6 ...+100 的和
'''

i=1
even=0
odd=0
while i<100:
    i=i+1
    if i%2==0:
        even=even+i
        print("even is",even)
    else:
        odd=odd+i
        print("odd is ",odd)
sum=even-odd
print("sunm is",sum)
print ("2-3+4­-5+6 ...+100 的和",even-odd)