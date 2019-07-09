#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基础3: 流程控制，条件 循环
'''
python 强制缩格，缩格部分都是执行块
注意if 和 else 后面都有：
for后面有冒号：
'''

age = 20
print('your age is: %d' % age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#if简写, 只要x是非零数值、非空字符串、非空list等
x = -1
if x:
    print('True')

#s = input('birth: ')
s = '1900'
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print(list(range(5)))

sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
    if n > 10:
        break
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
print(n)
