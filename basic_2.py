#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基础2: list
'''
注意3种括号区别：
{} : 定义对象
[] : 定义数组
() : 定义元组. 元组初始化后不能修改，不能赋值给其他变量
'''
classmate = ['Michael', 'Bob', 'Tim']
print(classmate)
print(len(classmate))
name = classmate[0]
print('%s' % name)
print(classmate[-1]) #-1表示倒数第一个，同理，-2表示倒数第二个

#追加到最后
classmate.append('Adam')
#添加到指定
classmate.insert(1, 'Jack')
#删除list末尾
classmate.pop()
#删除指定位置
classmate.pop(1)
print(classmate)

#list中的元素可以不同，甚至可以是另一个list
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print('array s length: %d' % len(s))

#元组
t = (1, 2)
print('the second value of t is %d' % t[1])

#定义一个只有1个元素的tuple，如果写成 t = (1)，系统认为括号是数学运算符，等价于 t = 1
#因此要写成t = (1,)。输出时也会带上逗号
t = (1,)
print(t)
