

import functools


def myfunc(a, b=2):

    print ' called myfunc with:', (a, b)
    return


def show_details(name, f, is_partial=False):
    print '%s:' % name
    print ' object:', f
    if not is_partial:
        print '__name__:', f.__name__
    if is_partial:
        print ' func:', f.func
        print ' args:', f.args
        print ' keywords:', f.keywords

    return

show_details('myfunc', myfunc)
myfunc('a', 3)
print

print '*' * 80

p1 = functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)

p1('passsing a ')
p1('override b', b=5)
print '*' * 80


p2 = functools.partial(myfunc, 'default a', b=99)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b;')
print
print '*' * 80

print 'Insufficient arguments:'
p1(1)
