#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# 函数: 最普通的定义和调用
'''
max(1,2,3) 接受多个参数，返回最大的
min(12,3,4)同理
'''
print(min(12,3,4))
#类型转换
print('int(\'123\') = %d' % int('123'))
'''
同理， float('12.34')， str(100)
'''
print('bool(1)')
print(bool(1))
print('bool(\'\')')
print(bool(''))

#给函数取别名
a = abs
print(a(-1))

#定义函数
def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if(x >= 0):
        return x
    else:
        return -x

print(myabs(-192))

#定义多个返回的函数。注意代码开头引入了import math
#返回的多个值实际上是个元组tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(12, 32, 49, 60)
print(x, y)
r = move(12, 32, 49, 60)
print(r)

'''
如果你已经把my_abs()的函数定义保存为abstest.py文件了，
那么，可以在该文件的当前目录下启动Python解释器，
用from abstest import my_abs来导入my_abs()函数，
注意abstest是文件名（不含.py扩展名）：
'''

#定义一个什么都不做的空函数
def nop():
    pass

#定义默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print('power(3) = %d' % power(3))

#默认参数的一个坑
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())    #返回：['END']
print(add_end())    #返回：['END', 'END']
print(add_end())    #返回：['END', 'END', 'END']

#默认参数也是变量，数组类型存的是指针。每次调用该函数时，指针没变，但指向的内容变了
#因此定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end_fix(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end_fix())    #返回：['END']
print(add_end_fix())    #返回：['END']

#定义可变参数, 即传入的参数个数可变
#参数前面加了*。函数内部，自动把参数转换为tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2))
print(calc())
nums = [1, 2, 3]
#把list当做可变参数传入
print(*nums)

#关键字参数， 允许传入任意多个键值对，在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

#使用预先组织好的dict
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#限制传入的参数
# *后面是必须出现的键值对。后面的参数如果缺少或多出来都会报错
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)
def person2(name, age, *, city, job):
    print(name, age, city, job)

args = (1, 2, 3, 4)
person1('person1', 24, *args, city='beijing', job='Engineer')
person2('person2', 24, city='beijing', job='Engineer')

#组合使用

def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person4('Jack', 24, job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, *args)
f1(1, 2, 3, *args, args =('a', 'b'))
f1(1, 2, 3, args =('a', 'b'), x=99)
f1(1, 2, 3, args =('a', 'b'), kw = {'x':99})


#递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
    
print(fact(10));