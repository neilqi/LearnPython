#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import package

'''
一般第三方库都会在Python官方的pypi.python.org网站注册
要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
pip install Pillow

或者使用Anaconda管理

试图加载一个模块时,python解释器会搜索当前目录、所有已安装的内置模块和第三方模块
搜索路径存放在sys模块的path变量中：

>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', ..., 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']

添加自己的搜索目录，
方法1，追加到sys.path后面
sys.path.append('/Users/michael/my_py_scripts')
方法2，设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中
'''