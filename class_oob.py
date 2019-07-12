#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#1 类的定义和使用
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.__score))
    
    def set_score(self, score):
        if 0 <= score <= 100:
            __score = score
        else:
            raise ValueError('bad score')


#创建对象
# __init__是构造函数
# 普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
# 调用时，不用传递该参数

me = Student('Neil', 60)
me.score = 90
me.print_score()
print(me.name)
# 属性名称前加__就变成了内部属性。
# me.__score 无法访问

'''
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
所以，仍然可以通过_Student__name来访问__name变量：

>>> bart._Student__name
'Bart Simpson'
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

最后注意下面的这种错误写法：

>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''

#2 继承
class Pupil(Student):
    def Pupil_run(self):
        print('pupils usually run a lot')

    def print_score(self):
        print('%s 得到一朵小红花' %  self.name)

pupil1 = Pupil('neilson', 90)
pupil1.print_score()
pupil1.Pupil_run()

class Player():
    def print_score(self):
        print('Player 取得进球')
# 多态
def showScore(Student):
    Student.print_score()

cr = Player()
showScore(me)
showScore(pupil1)
showScore(cr)
# 传入showScore的对象甚至可以不是Student或其子类，只要改对象拥有showScore用到的属性、方法即可


#3 获取对象信息
# 使用type()函数判断基本类型、变量指向的函数或类
'''
type(123)
<class 'int'>
type('123')
<class 'str'>
type(abs)
<class 'builtin_function_or_method'>
type(fn) == types.FuncitonType
type(abs) == types.BuilinFunctionType
type(lamda x: x) == types.LamdaType
type((x for x in range(1, 10))) == types.GeneratorType
'''
print(type(me))
print(type(pupil1))
print(type(cr))
'''
<class '__main__.Student'>
<class '__main__.Pupil'>
<class '__main__.Player'>
'''
# 使用isinstance() 可以判断继承关系,pupil1既是Pupil，还是Student
print(isinstance(pupil1, Pupil))            #True
print(isinstance(pupil1, Student))          #True

# 使用 dir() 获得对象的所有属性和方法
print(dir('abc'))
print(dir(pupil1))

'''
调用len()函数时，它自动去调用该对象的__len__()方法，所以下面的代码是等价的：
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
自定义类，如果也想用len(myObj)的话，实现__len__()方法即可

仅仅把属性和方法列出来是不够的，配合setattr(), getattr(), hasattr(),可以直接操作一个对象的状态
'''

class MyObject(object):
    name = 'Student'
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x^2


obj = MyObject()
print('测试obj对象的属性')
print('有属性%s吗? 结果: %s' % ('x', hasattr(obj, 'x')))
print('有属性%s吗? 结果: %s' % ('y', hasattr(obj, 'y')))
setattr(obj, 'y', 19)   #设置属性y
print('有属性%s吗? 结果: %s' % ('y', hasattr(obj, 'y')))
print('获取属性%s, 值：%s' % ('y', getattr(obj, 'y')))

print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404


# 实例属性与类属性
# 类属性是类内部定义的属性，实例属性是给实例对象赋值的属性，以MyObject为例
# x是MyObject内部定义的，所以是类属性
print(MyObject.name)    # 类属性 Student
obj.name = 'Neil'       # 实例属性，优先级高过类属性
print(obj.name)         # Neil
del obj.name            # 删除实例属性后，访问的就是类属性
print(obj.name)         # Student

class StudentPractice(object):
    count = 0
    def __init__(self, name):
        self.name = name
        StudentPractice.count += 1

if StudentPractice.count != 0:
    print('测试失败1!')
else:
    bart = StudentPractice('Bart')
    if StudentPractice.count != 1:
        print('测试失败2!')
    else:
        lisa = StudentPractice('Bart')
        if StudentPractice.count != 2:
            print('测试失败3!')
        else:
            print('Students:', StudentPractice.count)
            print('测试通过!')