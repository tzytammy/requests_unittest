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
    pass

#类的实例化
user11=Player('tom',100,'war')
user22=Player('hery',1000,'master')
user11.print_role()
user22.print_role()

user11.updateName('wilson')
user11.print_role()
user11.name=('aaa')
user11.print_role()