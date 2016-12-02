
class Singleton(object):

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, 'instance'):
            print 'hello'
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance



obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'

print obj1.attr1, obj2.attr1
print obj1 is obj2




# class FooParent(object):
#
#     def __init__(self):
#         self.parent = ' father'
#     def bar(self, msg):
#         print msg,'from father'
#
# class FooChild(object):
#     def __init__(self):
#         FooParent.__init__(self)
#         print 'son'
#
#     def bar(self, msg):
#         FooParent.bar(self, msg)
#         print 'son bar'
#         print self.parent


class FooParent(object):
    def __init__(self):
        self.parent = 'father'
        print 'father'

    def bar(self, msg):
        print msg, 'form father'


class FooChild(FooParent):

    def __init__(self):
        super(FooChild, self).__init__()
        print 'son'

    def bar(self, msg):
        super(FooChild, self).bar(msg)
        print 'son '
        print self.parent


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('hello world.')























