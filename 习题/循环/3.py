uneven = 0
for i in range(1,100):
    #方法1:得出的奇数-偶数+奇数-偶数....
    #方法2:求出奇数和，求出偶数和，用奇数和减偶数和
    if i % 2 == 1:
        print("1-99的奇数",i)
        uneven += i
    else:
        print("1-99的偶数",i)
        uneven -= i
print(uneven)   #得出结果