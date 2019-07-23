#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
functools使用说明
1. partial(funcname[, args][, *keywords])
如果原始函数参数多，可以使用partial创建新函数
固定住旧函数的部分参数，从而调用时更简单
'''
int2 = partial(int, base=2)
print(int2('11')) #二进制11转为整型

'''
2. update_wrapper 
用partial创建的对象没有__name__和__doc__
使用update_wrapper从原始对象拷贝复制到partial对象中去

3. wrapper
等同于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
定义装饰器，用于扩展函数功能；在函数运行前执行一些脚本
'''
#定义装饰器wrap3
def wrap3(func):
    @wraps(func)
    def call_it(*args, **kwargs):
        print('before call')
        return func(*args, **kwargs)
    return call_it

@wrap3
def hello3():
    print('hello world3')

hello3()