#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基础4: 字典
'''
    和list比较，dict有以下几个特点：
    
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：
    
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法
    
    set是一组key的集合，但不存储value。在set中，没有重复的key，重复元素在set中自动被过滤
'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#判断指定key是否存在
print('Thomas' in d)

print(d.get('Thomas')) #不存在返回null
print(d.get('Thomas', -1)) #不存在返回指定值-1
print(d.get('Bob'))
print('移除Bob')
d.pop('Bob')
print(d)

#set
s = set([1, 2, 3])
print(s)
#add添加，remove

#集合取交集，并集
s1 = set([1, 2, 3])
s2 = set([1, 2, 4])
print(s1 & s2)
print(s1 | s2)
