#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
else:
    print('当前环境不是命令行模式，__name__：%s' % __name__)

#1 模块
'''
以上为标准模块格式
第1行，让该文件可以直接在Unix/Linux/Mac上运行
第2行，表示.py文件本身使用标准UTF-8编码
第4行，表示该模块的文档注释
第6行，作者信息
第8行，引用

sys.argv 表示python命令接收的参数

λ python Package.py
Hello, world!

λ python Package.py Michael
Hello, Michael!

λ python Package.py Michael Scofiled
Too many arguments!

当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
如果在交互环境下或导入到其他文件中，命名为：package
'''

# 每一个包目录下面都会有一个__init__.py的文件
# 这个文件是必须存在的，否则，Python就把这个目录当成普通目录

#2 作用域
'''
_xxx：private
__xxx__: public，一般表示有特殊用途
xxx: public
'''