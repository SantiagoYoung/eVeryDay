


class BaseBase(object):
    def __init__(self, *args, **kwargs):
        print 'banana'
        super(BaseBase, self).__init__(*args, **kwargs)

class Base1(BaseBase):
    def __init__(self, *args, **kwargs):
        print 'base1'
        super(Base1, self).__init__(*args, **kwargs)

class Base2(BaseBase):
    def __init__(self, arg, *args, **kwargs):
        print 'base2'
        super(Base2, self).__init__(*args, **kwargs)

class MyClass(Base1, Base2):
    def __init__(self, arg):
        print 'my base'
        super(MyClass, self).__init__(arg)


m = MyClass(1)
print m