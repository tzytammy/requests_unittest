#题目1: 按照下面的格式打印1~10的数字以及每个数的平方、几何级数和阶乘

'''
数字      平方    三次方
1             1            1
2            4            8
3            9            27
4           16           64
5           25          125

'''

print("数学，  平方，   三次方 ")
for i in range(1,10):
    double=i*i
    tripple=i*i*i
    print(i,end='             ')
    print(double,end='              ')
    print(tripple)