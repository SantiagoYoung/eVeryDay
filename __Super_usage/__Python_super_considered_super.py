# coding=utf-8
import logging
import collections

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r' % (key, value))
        super(LoggingDict, self).__setitem__(key, value)

class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

# 继承树的结构是：　LoggingOD, LoggingDict, OrderedDIct, dict, object
#    OrderedDict 的位置是在　LoggingDict 和　dict 之间

# This means that the super() call in LoggingDict.__setitem__
# now dispatches the key/value update to OrderedDict instead of dict.

'''   Search Order  '''
# Method Resolution Order   =====   MRO

from pprint import pprint
pprint(LoggingOD.__mro__)

# MRO 的顺序，有以下几个方面的限制。
#   ! LoggingOD  在　LoggingDIct 和　OrderedDict 前面　
#   ! LoggingDict 在　OrderedDict 之前
#   ! LoggingDict 在　dict 之前
#   ! OrderedDict 在　dict 之前
#   ! dict  在　object  之前

'''
children precede their parents and the order of appearance in __bases__ is respected.

'''

# This presents three easily solved practical issues:
#
# the method being called by super() needs to exist
# the caller and callee need to have a matching argument signature
# and every occurrence of the method needs to use super()


#  1. 参数继承的问题
#  2. 确定方法确实存在
#  3.

class Root(object):
    def draw(self):
        assert not hasattr(super(Root, self), 'draw')


class Shape(Root):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super(Shape, self).__init__(**kwargs)
    def draw(self):
        print 'Drawing. Setting shape to:', self.shapename
        super(Shape, self).draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super(ColoredShape, self).__init__(**kwargs)
    def draw(self):
        print 'Drawing, Setting color to:', self.color
        super(ColoredShape, self).draw()

cs = ColoredShape(color='red', shapename='u')
cs.draw()


class Moveable(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print 'Drawing at position:', self.x, self.y

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwargs):
        self.movable = Moveable(x, y)
        super(MoveableAdapter, self).__init__(**kwargs)
    def draw(self):
        self.movable.draw()
        super(MoveableAdapter, self).draw()

class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass
print '*' * 45
MovableColoredShape(color='red', shapename='u', x=10, y=10).draw()
print MovableColoredShape.__mro__



from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__,
                           OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
print '*' * 49
oc = OrderedCounter('abcraccabdt')
print oc
print OrderedCounter.__mro__





















import re
_list = []

line = 'adf df, asdf, dsfds; sadfa'

result = re.match('(\w+)[,;\s]').group(1)
_list.append(result)








