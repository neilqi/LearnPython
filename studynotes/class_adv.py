#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#1 __slots__

'''
python允许给类和实例动态添加属性、方法。
给类添加的可以作用于所有对象，给实例添加进作用于当前对象
可以使用__slots__限制动态添加的属性、方法
'''
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Neil' #正常
# s.score = 90  #报错

#注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

#2 @property, 负责把一个方法变成属性。不定义setter就是只读属性
class StudentWithP(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在0到100之间')
        self._score = value

#3 多重继承 子类继承自多个父类

# 在设计类的继承关系时，通常，主线都是单一继承下来的。Dog继承自Mammal
# 习惯上把主线外加进来的父类命名为 xxMixIn
'''
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
'''

#4 定制类
'''
__len__(): 为了让类作用于len()函数
__str__(): 自定义输出，相当于实现了tostring
__repr__(): 自定义输出 直接显示变量调用的不是__str__()，而是__repr__()
            两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
            也就是说，__repr__()是为调试服务的
__iter__(): 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
            该方法返回一个迭代对象
            Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
            直到遇到StopIteration错误时退出循环
'''

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

'''
__getitem__(): 按照下标取出元素，需要实现__getitem__()方法
'''
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib2()
print(f[10])

# __getattr__(): 调用不存在的属性时返回默认值，或函数
class StudentWithGA(object):
    
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        else:
            raise AttributeError('\'StudentWithGA\' object has no attribute \'%s\'' % attr)

'''
现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：
'''
class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

Chain().status.user.timeline.list
# 返回 /status/user/timeline/list

'''
 __call__   一般的实例调用方法写法是：s.getscore()
            实现了__call__方法，就可以直接使用实例对象来调用，写法：s(xx)
'''
class studentCall(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self, score):
        print('%s score: %d' % (self.name, score))

scall = studentCall('neil')
scall(90)


#4 枚举
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#使用单个枚举
print(Month.Jan, Month.Jan.name, Month.Jan.value)
#遍历枚举。value属性是自动赋给成员的，默认从1开始
for name, member in Month.__members__.items():
    print(name, '=>', member, ', ', member.value)

#精确定义枚举, 使用@unique，保证枚举唯一
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 使用多种形式访问枚举
print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday(3))


# 引入类包
# import package_runoob.FileName
# 引入类包指定类
from package_runoob.FileName import ClassName

h = ClassName()
h.FuncName()

print(type(ClassName))
print(type(h))

# 使用type()方法定义类
def fun(self, name='world'):
    print('Hello %s' % name)

Hello = type('Hello', (object, ), dict(hello = fun))
            # 类名      父类        方法
htype = Hello()
htype.hello()

#metaclass 