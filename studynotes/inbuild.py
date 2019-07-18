#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

# namedtuple: 快速定义数据类型，'Point'可以看做类，['x', 'y']可以看做该类的属性
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,3)
print(p.x, p.y)

# deque 双向列表
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)


# defaultdic 当key不存在时的默认值
from collections import defaultdict
dd = defaultdict(lambda:'na')
dd['key1'] = 'abc'
print(dd['key2'])

# OrderedDict 有序字典，按插入顺序排列，而不是key的顺序
from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))


# ChainMap 把一组dict串起来并组成一个逻辑上的dict
from collections import ChainMap
import os, argparse

defaults = {
    'color': 'red',
    'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
# namespace 用于解析传入参数
# var() 返回对象的属性和属性值
# 生成器， 遍历所有传入参数，有值则保留
command_line_args = {k: v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)

print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 一个更简单直观的例子
a = {"x":1, "z":3}
b = {"y":2, "z":4}
c = ChainMap(a,b)
print(c)
print("x: {}, y: {}, z: {}".format(c["x"], c["y"], c["z"]))


# Counter 数组计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1


# MD5和sha1
import hashlib

md5 = hashlib.md5()
md5.update('111111'.encode('utf-8'))
#md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全
import hmac
message = b'111111'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())


# 迭代器，理论上可以创建无限的列表；实际通常使用takewhile取一部分
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# 自定义函数实现上下文管理, 通过__enter__和__exit__这两个方法实现
# class Query(object):
#     def __init__(self, name):
#         self.name = name
    
#     def __enter__(self):
#         print('begin')
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('error')
#         else:
#             print('end')
    
#     def query(self):
#         print('query info about %s...' % self.name)

# with Query('bob') as q:
#     q.query()

# __enter__和__exit__的简化写法
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    
    def query(self):
        print('query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')

with create_query('bob') as q:
    q.query()