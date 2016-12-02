# coding: utf-8

# 一、__init__ 方法是什么？
# __init__ 方法通常用在初始化一个类实例的时候。




# 二、__new__ 方法是什么？
# __new__方法正是创建这个类实例的方法。


class Person(object):

    def __new__(cls, name, age):
        print '__new__ called'
        return super(Person, cls).__new__(cls, name, age)

    def __init__(self, name, age):
        print '__init__ called'
        self.name = name
        self.age  = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':

    pig = Person('pig', 12)
    print pig


# 三、__new__ 的作用

# 依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)，
# 提供给你一个自定义这些类的实例化过程的途径。




class PositiveInteger(int):

    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))


i = PositiveInteger(-2)
print i

class ZPositiveInteger(int):

    def __new__(cls, value):
        return super(ZPositiveInteger, cls).__new__(cls, abs(value))

i = ZPositiveInteger(-3)
print i













