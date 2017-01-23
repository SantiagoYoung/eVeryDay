

def foo(x):
    print 'executing foo(%s)'%(x)

class A(object):

    def foo(self, x):
        print 'executing foo(%s, %s)' %(self, x)

    @classmethod
    def class_foo(cls, x):
        print 'executing class_foo(%s, %s)'%(cls,x)

    @staticmethod
    def static_foo(x):
        print 'executing static_foo(%s)'% x
a = A()
#
# a.foo(1)
# a.class_foo(1)
# A.class_foo(1)
# a.static_foo(1)
# A.static_foo(1)


def fibo(x):
    assert x > 0
    if x <= 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print fibo(3)

def fib(x):
    a = 0
    b = 1
    while a < x:
        yield a
        a, b = b, a+b

print list(fib(6))





