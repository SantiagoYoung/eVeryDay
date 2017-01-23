
import functools


def myfunc(a, b=2):
    print '   called myfunc wity:', (a, b)
    return



def show_details(name, f):
    print '%s' % name

    print '     object:', f
    print '     __name__:',
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print ' __doc__', repr(f.__doc__)
    print

    return

show_details('myfunc', myfunc)
print '*' * 80

p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)
print '*' * 80

print 'Updating wrapper:'
print ' assign:', functools.WRAPPER_ASSIGNMENTS
print ' update:', functools.WRAPPER_UPDATES
print


print '*' * 80

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)


