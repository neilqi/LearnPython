#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1. open() 读文件
# try:
#     f = open('README.md', 'r')
#     fc = f.read()
#     print(fc)
# finally:
#     if f:
#         f.close()

''' '''
''' '''
# with open('README.md', 'r') as f:
#     print(f.read())

# with open('README.md', 'r') as f:
#     for line in f.readlines():
#         print (line.strip())  # strip() 把末尾的换行删掉

# 二进制文件
# bf = open('io.png', 'rb')
# print(bf.read())

# 非utf-8文件，打开时需指定编码; 打开遇到错误可以忽略
# gf = open('gbk.txt', 'r', encoding='gbk', errors='ignore')

#2. 写文件
# f = open('test.txt', 'w')
# f.write('Hello world!')
# f.close()

# with open('test.txt', 'a', encoding='gbk') as f:
#     f.write('\nwith world')

''' '''
''' '''

#3. StringIO 在内存中读写字符串；BytesIO 操作二进制数据
from io import StringIO
# f = StringIO('this is a IOString Test \n')
# f.write('hello')
# f.write(' ')
# f.write('world')
# #print(f.getvalue())

# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

''' '''
''' '''

import os
print(os.name)      #posix: Linux、Unix或Mac OS X，nt: Windows系统
# print(os.environ)   #所有的环境变量
# print(os.environ.get('APPDATA'))    #获取指定环境变量
# print(os.path.abspath('.'))     #当前路径
# path = os.path.join(os.path.abspath('.'), 'testdir')
# if os.path.isdir(path):
#     os.removedirs(path)
# else:
#     os.mkdir(path)

'''
os.path.split() 把路径拆分成目录 和 文件名
os.path.splittext 拆分出文件扩展名
os.rename 改名
os.remove 删除文件
'''
# 过滤出指定类型文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.md'])

import pickle

# if not os.path.isfile(os.path.join(os.path.abspath('.'), 'dump.txt')):
#     d = dict(name='Bob', age=20, socre=80)
#     print(pickle.dumps(d))
#     # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
#     # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
#     f = open('dump.txt', 'wb')
#     pickle.dump(d, f)
#     f.close()
# else:
#     f = open('dump.txt', 'rb')
#     d = pickle.load(f, encoding='utf-8')
#     f.close()
#     print(d)


# JSON

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 80)
# print(json.dumps(s))

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=lambda obj: obj.__dict__, ensure_ascii=True))