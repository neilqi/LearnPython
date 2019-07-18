#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

#如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
#过滤掉指定字符
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
#分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))       #注意到group(0)永远是原始字符串
print(m.group(1))
print(m.group(2))

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 非贪婪匹配 也就是尽可能少匹配 加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

    