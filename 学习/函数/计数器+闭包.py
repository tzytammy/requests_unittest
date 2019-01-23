def counter():
    cnt=[0]
    def add_one():
        cnt[0]+=1
        return  cnt[0]

    return  add_one
num1=counter()
print(num1())
print(num1())
print(num1())
print(num1())
