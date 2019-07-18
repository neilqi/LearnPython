#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print absolute value of an integer:
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*- 指定编码模式
这是多行注释，用三个单引号或三个双引号
这是多行注释，用三个单引号 
'''
a = 100
if a >= 0:
	print(a)
else:
	print(-a)

# ord函数获取字符的整数， chr函数将整数转为字符
print(ord('A'))
print(chr(25991))
print('\u4e2d\u6587')
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('中文'))

#格式化输出
print('Hi, %s, you have %2d pc, and %.2f 元. growth rate: %d %%' % ('Michael', 1, 100.00, 70))
print('Hello, {0}, the money is: {1:.2f} yuan'.format('小米', 17.123))