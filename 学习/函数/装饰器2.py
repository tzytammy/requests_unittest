#带参数模板
def tips(func):
    def nei(a,b):
        print("start")
        func(a,b)
        print("stop")
        return 'i am here'
    return nei


@tips
def add(a,b):
    print(a+b)
@tips
def sum(a,b):
    print(a-b)

print(add(4,5))
print(sum(9,6))