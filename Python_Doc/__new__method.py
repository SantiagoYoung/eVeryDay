# coding=utf-8


# __new__() 方法的特性：
#
#       __new__() 方法是在类准备将自身实例化时调用。
#       __new__() 方法始终都是类的静态方法，即使没有被加上静态方法装饰器。




def __new__(cls, *args, **kwargs):
    super(cls, *args, **kwargs)
    pass
# cls 是当前正在实例化的类．

# 通常来说，新式类开始实例化时，__new__()
# 方法会返回cls（cls指代当前类）的实例，然后该类的__init__()
# 方法作为构造方法会接收这个实例（即self）作为自己的第一个参数，然后依次传入__new__()
# 方法中接收的位置参数和命名参数。



class Demo(object):
    def __init__(self, x):
        print '\n__init__() called....{}'.format(self)

    def __new__(cls, *args, **kwargs):

        print '\n__new__() called ... {}'.format(cls)
        return super(Demo, cls).__new__(cls, *args, **kwargs)

de = Demo(1)

# __new__()必须要有返回值，返回实例化出来的实例
# 若__new__()没有正确返回当前类cls的实例，那__init__()将不会被调用，即使是父类的实例也不行。


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

ob1 = Singleton()
ob2 = Singleton()

print id(ob1) == id(ob2)
# ob1.attr = 'value'
# print ob1.attr, ob2.arr
print ob1 is ob2









