import inspect

def a(a, b=0, *c, d, e=1, **f):
    pass

aa = inspect.signature(a)
print("inspect.signature(fn)是:%s" % aa)
print("inspect.signature(fn)的类型：%s" % (type(aa)))
print("\n")

bb = aa.parameters
print("signature.paramerters属性是:%s" % bb)
print("ignature.paramerters属性的类型是%s" % type(bb))
print("\n")

for cc, dd in bb.items():
    print("mappingproxy.items()返回的两个值分别是：%s和%s" % (cc, dd))
    print("mappingproxy.items()返回的两个值的类型分别是：%s和%s" % (type(cc), type(dd)))
    print("\n")
    ee = dd.kind
    print("Parameter.kind属性是:%s" % ee)
    print("Parameter.kind属性的类型是:%s" % type(ee))
    print("\n")
    gg = dd.default
    print("Parameter.default的值是: %s" % gg)
    print("Parameter.default的属性是: %s" % type(gg))
    print("\n")


ff = inspect.Parameter.KEYWORD_ONLY
print("inspect.Parameter.KEYWORD_ONLY的值是:%s" % ff)
print("inspect.Parameter.KEYWORD_ONLY的类型是:%s" % type(ff))


# 参数类型为VAR_POSITIONAL时，即*args参数，只能通过位置传值
def say_hello(*args):
    print('hello {0}'.format(args))

# 通过位置传值
say_hello('jack', 'tom')

# 参数类型为VAR_KEYWORD，即 **kwargs参数，只能通过关键字传值，如

def func_b(**kwargs):
    print(kwargs)

# 通过关键字传值
func_b(a=1, b=2)

# 参数类型为KEYWORD_ONLY时，说明此参数前面存在VAR_POSITIONAL类型的参数，只能通过关键字传值，如

def func_b(*args, a, b):
    print(args, a, b)

# 只能通过关键字传值
func_b('test', a=1, b=2)