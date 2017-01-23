
class BaseBase(object):
    def method(self):
        print 'banana'
class Base1(BaseBase):
    pass
class Base2(BaseBase):
    def method(self):
        print 'Base2'

class Myclass(Base1, Base2):
    pass

here = Myclass()
print here.method()
print Myclass.__mro__
def L(klass):
    return [k.__name__ for k in klass.__mro__]

print L(Myclass)









