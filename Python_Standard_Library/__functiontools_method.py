
import functools

class MyClass(object):

    def method1(self, a, b=2):
        print ' called method1 with:', (self, a, b)
        return

    def method2(self, c, d=-5):
        print ' called mwthod2 with:', (self, c, d)
        return

    wrapped_method2 = functools.partial(method2, 'wrapped c')
    functools.update_wrapper(wrapped_method2, method2)

    def __call__(self, e, f=6):
        print ' called object with:', (self, e, f)
        return


def show_details(name, f):
    print '%s' % name
    print ' object:', f
    print '__name__',
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print ' __doc__', repr(f.__doc__)
    return

o = MyClass()

show_details('method1 straight', o.method1)
o.method1('no default for a ', b=3)

print '*' * 80


p1 = functools.partial(o.method1, b=4)
functools.update_wrapper(p1, o.method1)
show_details('method1 wrapper', p1)
p1('a goes here')

print '*' * 80

show_details('method2', o.method2)
o.method2('no default for c', d=6)

print '*' * 80

show_details('wrapped method2', o.wrapped_method2)
o.wrapped_method2('no default for c', d=6)

print '*' * 80

show_details('instance', o)
o('no default for e')

print '*' * 80

p2 = functools.partial(o, f=7)
show_details('instance wrapper', p2)
p2('e goes here')
print '*' * 80
