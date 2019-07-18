#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
#1 python 的错误处理机制
try:
    print('try...')
    r = 10 / 0
    print('result...')
except ZeroDivisionError as e:
    print('catch exception: ', e)
finally:
    print('finally')
print('end')

# 用assert代替print 输出调试信息

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    foo('0')

'''
#assert的意思是：n应该不等于0。
#如果断言不成立，就抛出断言异常，同时输出 'n is zero'
#AssertionError: n is zero!
#python -O debug.py 关闭断言 -O 是大写字母O，不是数字0
'''

#2 可以用logging 记录错误日志
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10/n)

# python -m pdb debug.py
# -m pdb 进入单步运行模式
'''
#l 查看代码; p 变量名， 查看变量; n 单步执行； q 退出
''' 
# pdb.set_trace() 加入断点
# 可以用命令p查看变量，或者用命令c继续运行
import pdb
spdb = '0'
npdb = int(spdb)
pdb.set_trace()
print(10 / npdb)

'''

#3 单元测试
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

import unittest


class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法    
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertTrue('key', 'value')
    
    def test_attr(self):
        d = Dict()
        d.keys = 'value'
        self.assertTrue('key'in d)
        self.assertEqual(d['key'], 'value')
        
    #期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()


'''
setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
'''