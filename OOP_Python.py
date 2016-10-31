# -*- coding: utf-8 -*-
"""类与面向对象----类与面向对象----类与面向对象----类与面向对象----类与面向对象----类与面向对象----类与面向对象----类与面向对象----类与面向对象----类与面向对象"""

#-- 最普通的类
class C1(C2, C3):

    spam = 32                   # 数据属性
    def __init__(self, name):   # 函数属性:构造函数
        self.name = name
    def __del__(self):          # 函数属性:析构函数
        print ('goodbye', self.name)
I1 = C1('bob')



#-- Python的类没有基于参数的函数重载
    class FirstClass:
        def test(self, string):
            print(string)
        def test(self):                 # 此时类中只有一个test函数 即后者test(self) 它覆盖掉前者带参数的test函数
            print("hello world")


#-- 子类扩展超类: 尽量调用超类的方法
    class Manager(Person):
        def giveRaise(self, percent, bonus = .10):
            self.pay = int(self.pay*(1 + percent + bonus))     # 不好的方式 复制粘贴超类代码
            Person.giveRaise(self, percent + bonus)            # 好的方式 尽量调用超类方法



#-- 类内省工具
    bob = Person('bob')
    bob.__class__                       # <class 'Person'>
    bob.__class__.__name__              # 'Person'
    bob.__dict__                        # {'pay':0, 'name':'bob', 'job':'Manager'}




#-- 返回1中 数据属性spam是属于类 而不是对象
    I1 = C1('bob'); I2 = C2('tom')      # 此时I1和I2的spam都为42 但是都是返回的C1的spam属性
    C1.spam = 24                        # 此时I1和I2的spam都为24
    I1.spam = 3                         # 此时I1新增自有属性spam 值为2 I2和C1的spam还都为24




#-- 类方法调用的两种方式
    instance.method(arg...)
    class.method(instance, arg...)



    # -- 抽象超类的实现方法
    # (1)某个函数中调用未定义的函数 子类中定义该函数


def delegate(self):
    self.action()  # 本类中不定义action函数 所以使用delegate函数时就会出错
    # (2)定义action函数 但是返回异常


def action(self):
    raise NotImplementedError("action must be defined")
    # (3)上述的两种方法还都可以定义实例对象 实际上可以利用@装饰器语法生成不能定义的抽象超类


from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    @abstractmethod
    def action(self): pass


x = Super()  # 返回 TypeError: Can't instantiate abstract class Super with abstract methods action




#-- # OOP和继承: "is-a"的关系
    class A(B):
        pass
    a = A()
    isinstance(a, B)                    # 返回True, A是B的子类 a也是B的一种
    # OOP和组合: "has-a"的关系
    pass
    # OOP和委托: "包装"对象 在Python中委托通常是以"__getattr__"钩子方法实现的, 这个方法会拦截对不存在属性的读取
    # 包装类(或者称为代理类)可以使用__getattr__把任意读取转发给被包装的对象
    class wrapper:
        def __init__(self, object):
            self.wrapped = object
        def __getattr(self, attrname):
            print('Trace: ', attrname)
            return getattr(self.wrapped, attrname)
    # 注:这里使用getattr(X, N)内置函数以变量名字符串N从包装对象X中取出属性 类似于X.__dict__[N]
    x = wrapper([1, 2, 3])
    x.append(4)                         # 返回 "Trace: append" [1, 2, 3, 4]
    x = wrapper({'a':1, 'b':2})
    list(x.keys())                      # 返回 "Trace: keys" ['a', 'b']

#-- 类的伪私有属性:使用__attr
    class C1:
        def __init__(self, name):
            self.__name = name          # 此时类的__name属性为伪私有属性 原理 它会自动变成self._C1__name = name
        def __str__(self):
            return 'self.name = %s' % self.__name
    I = C1('tom')
    print(I)                            # 返回 self.name = tom
    I.__name = 'jeey'                   # 这里无法访问 __name为伪私有属性
    I._C1__name = 'jeey'                # 这里可以修改成功 self.name = jeey



#-- 类方法是对象:无绑定类方法对象 / 绑定实例方法对象
    class Spam:
        def doit(self, message):
            print(message)
        def selfless(message)
            print(message)
    obj = Spam()
    x = obj.doit                        # 类的绑定方法对象 实例 + 函数
    x('hello world')
    x = Spam.doit                       # 类的无绑定方法对象 类名 + 函数
    x(obj, 'hello world')
    x = Spam.selfless                   # 类的无绑定方法是函数 在3.0之前无效
    x('hello world')

#-- 获取对象信息: 属性和方法
    a = MyObject()
    dir(a)                              # 使用dir函数
    hasattr(a, 'x')                     # 测试是否有x属性或方法 即a.x是否已经存在
    setattr(a, 'y', 19)                 # 设置属性或方法 等同于a.y = 19
    getattr(a, 'z', 0)                  # 获取属性或方法 如果属性不存在 则返回默认值0
    #这里有个小技巧，setattr可以设置一个不能访问到的属性，即只能用getattr获取
    setattr(a, "can't touch", 100)      # 这里的属性名带有空格，不能直接访问
    getattr(a, "can't touch", 0)        # 但是可以用getattr获取



#-- 为类动态绑定属性或方法: MethodType方法
    # 一般创建了一个class的实例后, 可以给该实例绑定任何属性和方法, 这就是动态语言的灵活性
    class Student(object):
        pass
    s = Student()
    s.name = 'Michael'                  # 动态给实例绑定一个属性
    def set_age(self, age):             # 定义一个函数作为实例方法
        self.age = age
    from types import MethodType
    s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法 类的其他实例不受此影响
    s.set_age(25)                       # 调用实例方法
    Student.set_age = MethodType(set_age, Student)    # 为类绑定一个方法 类的所有实例都拥有该方法



"""类的高级话题----类的高级话题----类的高级话题----类的高级话题----类的高级话题----类的高级话题----类的高级话题----类的高级话题----类的高级话题----类的高级话题"""

#-- 多重继承: "混合类", 搜索方式"从下到上 从左到右 广度优先"
    class A(B, C):
        pass


#-- 类的继承和子类的初始化
    # 1.子类定义了__init__方法时，若未显示调用基类__init__方法，python不会帮你调用。
    # 2.子类未定义__init__方法时，python会自动帮你调用首个基类的__init__方法，注意是首个。
    # 3.子类显示调用基类的初始化函数：
    class FooParent(object):
        def __init__(self, a):
            self.parent = 'I\'m the Parent.'
            print('Parent:a=' + str(a))
        def bar(self, message):
            print(message + ' from Parent')
    class FooChild(FooParent):
        def __init__(self, a):
            FooParent.__init__(self, a)
            print('Child:a=' + str(a))
        def bar(self, message):
            FooParent.bar(self, message)
            print(message + ' from Child')
    fooChild = FooChild(10)
    fooChild.bar('HelloWorld')





#-- #实例方法 / 静态方法 / 类方法
    class Methods:
        def imeth(self, x): print(self, x)      # 实例方法：传入的是实例和数据，操作的是实例的属性
        def smeth(x): print(x)                  # 静态方法：只传入数据 不传入实例，操作的是类的属性而不是实例的属性
        def cmeth(cls, x): print(cls, x)        # 类方法：传入的是类对象和数据
        smeth = staticmethod(smeth)             # 调用内置函数，也可以使用@staticmethod
        cmeth = classmethod(cmeth)              # 调用内置函数，也可以使用@classmethod
    obj = Methods()
    obj.imeth(1)                                # 实例方法调用 <__main__.Methods object...> 1
    Methods.imeth(obj, 2)                       # <__main__.Methods object...> 2
    Methods.smeth(3)                            # 静态方法调用 3
    obj.smeth(4)                                # 这里可以使用实例进行调用
    Methods.cmeth(5)                            # 类方法调用 <class '__main__.Methods'> 5
    obj.cmeth(6)                                # <class '__main__.Methods'> 6



#-- 函数装饰器:是它后边的函数的运行时的声明 由@符号以及后边紧跟的"元函数"(metafunction)组成
        @staticmethod
        def smeth(x): print(x)
    # 等同于:
        def smeth(x): print(x)
        smeth = staticmethod(smeth)
    # 同理
        @classmethod
        def cmeth(cls, x): print(x)
    # 等同于
        def cmeth(cls, x): print(x)
        cmeth = classmethod(cmeth)


#-- 类修饰器:是它后边的类的运行时的声明 由@符号以及后边紧跟的"元函数"(metafunction)组成
        def decorator(aClass):.....
        @decorator
        class C:....
    # 等同于:
        class C:....
        C = decorator(C)


#-- 限制class属性: __slots__属性
    class Student:
        __slots__ = ('name', 'age')             # 限制Student及其实例只能拥有name和age属性
    # __slots__属性只对当前类起作用, 对其子类不起作用
    # __slots__属性能够节省内存
    # __slots__属性可以为列表list，或者元组tuple



#-- 类属性高级话题: @property
    # 假设定义了一个类:C，该类必须继承自object类，有一私有变量_x
    class C(object):
        def __init__(self):
            self.__x = None
    # 第一种使用属性的方法
        def getx(self):
            return self.__x
        def setx(self, value):
            self.__x = value
        def delx(self):
            del self.__x
        x = property(getx, setx, delx, '')
    # property函数原型为property(fget=None,fset=None,fdel=None,doc=None)
    # 使用
    c = C()
    c.x = 100                         # 自动调用setx方法
    y = c.x                           # 自动调用getx方法
    del c.x                           # 自动调用delx方法
    # 第二种方法使用属性的方法
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
           self.__x = value
        @x.deleter
        def x(self):
           del self.__x
    # 使用
    c = C()
    c.x = 100                         # 自动调用setter方法
    y = c.x                           # 自动调用x方法
    del c.x                           # 自动调用deleter方法


#-- 定制类: 重写类的方法
    # (1)__str__方法、__repr__方法: 定制类的输出字符串
    # (2)__iter__方法、next方法: 定制类的可迭代性
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1     # 初始化两个计数器a，b
        def __iter__(self):
            return self               # 实例本身就是迭代对象，故返回自己
        def next(self):
            self.a, self.b = self.b, self.a + self.b
            if self.a > 100000:       # 退出循环的条件
                raise StopIteration()
            return self.a             # 返回下一个值
    for n in Fib():
        print(n)                      # 使用
    # (3)__getitem__方法、__setitem__方法: 定制类的下标操作[] 或者切片操作slice
    class Indexer(object):
        def __init__(self):
            self.data = {}
        def __getitem__(self, n):             # 定义getitem方法
            print('getitem:', n)
            return self.data[n]
        def __setitem__(self, key, value):    # 定义setitem方法
            print('setitem:key = {0}, value = {1}'.format(key, value))
            self.data[key] = value
    test = Indexer()
    test[0] = 1;   test[3] = '3'              # 调用setitem方法
    print(test[0])                            # 调用getitem方法



# (4)__getattr__方法: 定制类的属性操作
    class Student(object):
        def __getattr__(self, attr):          # 定义当获取类的属性时的返回值
            if attr=='age':
                return 25                     # 当获取age属性时返回25
        raise AttributeError('object has no attribute: %s' % attr)
        # 注意: 只有当属性不存在时 才会调用该方法 且该方法默认返回None 需要在函数最后引发异常
    s = Student()
    s.age                                     # s中age属性不存在 故调用__getattr__方法 返回25





#  (5)__call__方法: 定制类的'可调用'性
class Student(object):
    def __call__(self):  # 也可以带参数
        print('Calling......')


s = Student()
s()  # s变成了可调用的 也可以带参数
callable(s)  # 测试s的可调用性 返回True


#    (6)__len__方法：求类的长度
def __len__(self):
    return len(self.data)



#-- 动态创建类type()
    # 一般创建类 需要在代码中提前定义
        class Hello(object):
            def hello(self, name='world'):
                print('Hello, %s.' % name)
        h = Hello()
        h.hello()                             # Hello, world
        type(Hello)                           # Hello是一个type类型 返回<class 'type'>
        type(h)                               # h是一个Hello类型 返回<class 'Hello'>
    # 动态类型语言中 类可以动态创建 type函数可用于创建新类型
        def fn(self, name='world'):           # 先定义函数
            print('Hello, %s.' % name)
        Hello = type('Hello', (object,), dict(hello=fn))
        # 创建Hello类 type原型: type(name, bases, dict)
        h = Hello()                           # 此时的h和上边的h一致


















































































































































































































































