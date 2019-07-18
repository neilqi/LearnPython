#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
'''
将函数作为结果返回
'''
#1 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1,3,4,5,6)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    #print(fs)
    return fs

f1, f2, f3 = count()
#左侧是简写的列表，f1, f2, f3分别对应fs[]的三个元素
print(f1())
print(f2())
print(f3())

# f1(),f2(),f3()调用结果都是9
# 原因是三个闭包中的i来自同一个变量, 在执行时i在内存中存的值为3


#2 匿名函数（lamda）
# 传入lamda
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 将lamda赋给变量
fa = lambda x: x*x
print(fa(5))

# 将lamda作为返回值
def build(x, y):
    return lambda: x*x + y*y

fb = build(3, 4)
print(fb())


#3 装饰器 decorator. 本质上就是个返回函数。
# 传入参数是要装饰的函数，返回的参数是要执行的额外功能
# 时间操作需引入time。 import time
def log(func):
    def wrapper(*args, **kw):
        print('before call %s(), do something' % func.__name__)
        result = func(*args, **kw)
        print('after call %s(), do something else' % func.__name__)
        return result
    return wrapper
#@log 相当于执行了语句 now = log(now)
# 函数对象有一个__name__属性，可以拿到函数的名字

@log   
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
dstr = now()
print(dstr)

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def logWithText(logtext):
    def decorator(func):
        def wrapper(*args, **kw):
            print('before call %s(), log info: ' % func.__name__, logtext)
            result = func(*args, **kw)
            print('after call %s(), log info: ' % func.__name__, logtext)
            return result
        return wrapper
    return decorator
                
@logWithText('调用新日期now2')
def now2():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
dstr2 = now2()
print(dstr2)

#4 偏函数 预先定义某函数的部分参数，简化参数调用
# 简化int函数，该函数的参数base预制为2
import functools
int2 = functools.partial(int, base=2)

print(int2('1010111001'))

'''
创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
当传入：int2 = functools.partial(int, base=2)
实际上固定了int()函数的关键字参数base，相当于：
kw = { 'base': 2 }
int('10010', **kw)

当传入：max2 = functools.partial(max, 10)
实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7) 相当于：
args = (10, 5, 6, 7)
max(*args)
结果为10。
'''