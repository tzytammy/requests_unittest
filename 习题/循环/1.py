even = 0
count = 1
while count<100:
    count+=1
    #方法1：得出偶数-奇数+偶数-奇数...
    #方法2：求出所有的偶数减去所有的奇数和 （跟小学的换位运算类似）
    if count % 2 == 0:
        print("2-100的偶数",count)
        even += count
    else:
        print("2-100的奇数",count)
        even -= count
print(even) #得出的结果