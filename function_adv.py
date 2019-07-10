#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
#1. 切片操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0: 3])  #从0开始，取3个['Michael', 'Sarah', 'Tracy']
print(L[-1])    #倒数第1个Jack
print(L[-2:])   #从倒数第2个，取到list末尾['Bob', 'Jack']
print(L[-3:-2]) #从倒数第3个取到 倒数第2个左面 ['Tracy']
print(L[-3:-1]) #从倒数第3个取到 倒数第1个左面 ['Tracy', 'Bob']

L1 = list(range(100))
print(L1[:10:2]) #从第0个，到第10个，间隔2个数 [0, 2, 4, 6, 8]

#tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[::2])

#2. 迭代操作  for in
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('%s: %s' % (key, d[key]))

# 同理，字符串也可以迭代。  for ch in 'ABC':
# dict没有顺序，输出的顺序可能不一样
# dict 直接迭代时迭代的是key for key in d:
# 如果要迭代value，可以用 for value in d.values()
# 同时迭代键值对，用 for key, value in d.items()

# 判断一个对象是否可迭代
print(isinstance('abc', Iterable) )

# enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)


#3. 列表生成式
'''
如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)

列表生成式则可以用一行语句代替循环生成上面的list：
'''
L2 = [x * x for x in range(1, 11)]
print(L2)

#加条件，生成偶数平方
L3 = [x *x for x in range(1, 11) if x % 2 == 0]
print(L3)

#两层循环
L4 = [m+n for m in 'ABCDEFG' for n in '1234567890']
print(L4)

#列出当前目录下所有文件和目录名
import os
L5 = [d for d in os.listdir('.')]
print(L5)


#4. 生成器generator 存储数列的生成算法，而不是存具体的值
genList = (x * x for x in range(0, 10) if x % 2 == 0)
'''
print(next(genList))
print(next(genList))
print(next(genList))
next方法从第一个元素开始遍历，遍历后自动加一。超出范围会报错
'''
for genItem in genList:
    print(genItem)

'''
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
这里最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
再次执行时从上次返回的yield语句处继续执行。
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield  b
        a, b = b, a+b
        n += 1
    return 'done'

'''
fibList = fib(10)
print(next(fibList))
print(next(fibList))
'''
for genItem in fib(10):
    print(genItem)

#用for循环拿不到fib方法的return值。如果要获取return，需要使用StopIteration

gwithreturn = fib(6)
while True:
    try:
        x = next(gwithreturn)
        print('the value is ', x)
    except StopIteration as e:
        print('generator return value: ', e.value)
        break;
