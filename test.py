#coding=utf-8

def print_score(**kw):
    print(" Name  Score")
    print("------------------")
    for name,score in  kw.items():
        print ('%10s  %d' % (name, score))
print_score(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}
print_score(**data)


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)

x=int(input("一个数字"))
if x % 2:
    print ("x不可以被2整除")
else:
    print("x可以被2整除")