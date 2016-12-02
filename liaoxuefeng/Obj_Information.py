# coding: utf-8

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？


# 使用type()

print type(123)
print type('str')
print type(None)

# 但是type()函数返回的是什么类型呢？
# 它返回type类型。

# Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：


import types

print type('ac') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TupleType

# 最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：
# >>> type(int)==type(str)==types.TypeType
# True

# 使用isinstance()

# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：

# >>> isinstance('a', (str, unicode))
# True
# >>> isinstance(u'a', (str, unicode))
# True


# 由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：

# >>> isinstance(u'a', basestring)
# True

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):

    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print hasattr(obj, 'x')
print obj.x
print hasattr(obj, 'y')

setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y

# 如果试图获取不存在的属性，会抛出AttributeError的错误：

# 可以传入一个default参数，如果属性不存在，就返回默认值：

print getattr(obj, 'z', 404)


# 也可以获得对象的方法：

print hasattr(obj, 'power')

print getattr(obj, 'power')

fn = getattr(obj, 'power')
print fn
print fn()



































