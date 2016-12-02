

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('no')
        if value < 0 or value > 100:
            raise ValueError('nonono')
        self._score = value

s = Student()
s.set_score(60)
print s.get_score()


class StudentA(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('no')
        if value < 0 or value > 100:
            raise ValueError('nonono')
        self._score = value

S = StudentA()
S.score =60
print S.score


# How does the @property decorator work?
# This example is from the documentation:

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I am the 'x' property.")

# property's arguments are getx, setx, delx and a doc string.

# In the code below property is used as decorator.
# The object of it is the x function,
# but in the code above
# there is no place for an object function in the arguments.

class D(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def __xor__(self):
        del self._x


class Example(object):

    def __init__(self, value):
        self._val = value

    def _val_getter(self):
        return self._val

    def _val_setter(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._val = value

    def _val_deleter(self):
        del self._val

    val = property(fget=_val_getter, fset=_val_setter,
                   fdel=_val_deleter, doc=None)





# Descriptor - manage attributes

class Integer(object):
    def __init__(self, name):
        self._name = name

    def __get__(self, inst, cls):
        if inst is None:
            return self
        else:
            return inst.__dict__[self._name]

    def __set__(self, inst, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        inst.__dict__[self._name] = value

    def __delete(self, inst):
        del inst.__dict__[self._name]

class Exa(object):
    s = Integer('x')
    def __init__(self, val):
        self.x = val

ex1 = Exa(1)
print ex1.x, '>>>>>.'
ex2 = Exa('str')
print ex2
ex3 = Exa(3)
print hasattr(ex3, 'x')
del ex3.x
print hasattr(ex3, 'x')





# Abstract method - Metaclass

from abc import ABCMeta, abstractmethod

class base(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def absmethod(self):
        '''Abs method'''
class New(base):
    def absmethod(self):
        print 'abstract'

ex = New()
print ex.absmethod()

































