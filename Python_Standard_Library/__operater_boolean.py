







from operator import *


a = -1
b = 5

print 'a = ', a
print 'b = ', b
print


print 'not_(a)  :', not_(a)
print 'truth(a) :', truth(a)
print 'is_(a, b)   :', is_(a, b)
print 'is_not(a, b):', is_not(a, b)





for func in (lt, le, eq, ne, ge, gt):
    print '%s(a, b):' % func.__name__, func(a, b)





























