#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

'''
函数名其实就是指向函数的变量！
对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
>>> f = abs
>>> f(-10)
10
如果把abs指向其他对象，会有什么情况发生？
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

由于abs函数实际上是定义在import builtins模块中的，
所以要让修改abs变量的指向在其它模块也生效，
要用import builtins; builtins.abs = 10
'''
def absAdd(x, y, f):
    return f(x) + f(y)

print(absAdd(-3, -9, abs))

#2 map() reduce()
# 新列表 = map(函数，列表) 作用是把f(x)作用在list的每一个元素并把结果生成一个新的list
def f(x):
    return x * x
newList = map(f, [1,2,3,4,5,6,7])
print(list(newList))

# 把列表中的整数转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def fun_add(x, y):
    return x+y
print(reduce(fun_add, [1, 3, 5, 7, 9]))

# reduce + map 组合使用
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
  return digits[s]

def str2num(s):
  return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print('237892')

#3 filter()
# filter()也接收一个函数和一个序列。把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 过滤出奇数
def is_odd(n):
  return n % 2 == 1
print(list(filter(is_odd, list(range(100)))))

# 过滤掉空串 ''表示false
def not_empty(s):
    return s and s.strip()
