# coding=utf-8
'''
super 指的是ＭＲＯ中的下一个类！

ＭＲＯ： Method Resolution Order.

'''
'''
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
'''
class Root(object):
    def __init__(self):
        print 'this is root.'

class B(Root):
    def __init__(self):
        print 'enter B'
        super(B, self).__init__()
        print 'leave B'

class C(Root):
    def __init__(self):
        print 'Enter C'
        super(C, self).__init__()
        print "Leave C"

class D(B, C):
    pass


d = D()

print d.__class__
print d.__class__.__mro__

















