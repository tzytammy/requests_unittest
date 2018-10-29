#面向对象

class Player():   #定义一个类（把相似的进行归类）
    def __init__(self,name,hp,occu):  #self=user1，user2
        self.__name=name   #变量被称作属性
        self.hp=hp
        self.occu=occu
    def print_role(self):   #定义一个方法
        print('%s:%s,%s'%(self.__name,self.hp,self.occu))
    def updateName(self,newname):
        self.name=newname
class Monster():
    '定义怪物类'
    def __init__(self,hp=100):
        self.hp=hp
    def run(self):
        print('移动到某个位置')
    def whoami(self):
        print('我是怪物父类')

class Animals(Monster):
    '普通怪物'
    def __init__(self,hp=10):   #避免重复定义
        super().__init__(hp)


class Boss(Monster):

    'BOSS类怪物'
    def __init__(self,hp=950):   #避免重复定义
        super().__init__(hp)
    def whoami(self):
        print('我是boss 怪物')

a1=Monster(200)
print(a1.hp)
print(a1.run())
a2=Animals(1)
print(a2.hp)
print(a2.run())
a3=Boss(900)
a3.whoami()


#判断父类子类

print('a1的类型 %s'%type(a1))
print('a2的类型 %s'%type(a2))
print('a3的类型 %s'%type(a3))

#a2是否是Moster的子类
print(isinstance(a2,Monster))