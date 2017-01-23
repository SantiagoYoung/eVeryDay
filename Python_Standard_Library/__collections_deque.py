


import collections




d = collections.deque('abcdefg')
print 'Deque:', d
print "Length:", len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

print d.remove('c')

print 'remove(c):', d

print '*' * 69

d1 = collections.deque()
d1.extend('abcdefg')
print 'extend:', d1
d1.append('h')
print 'append   :', d1

print '&' * 80
d2 = collections.deque()
d2.extendleft(xrange(6))
print 'extendleft:', d2
d2.appendleft(6)
print 'appendleft:', d2

print '$' * 80
d3 = collections.deque('abcdefg')
while True:
    try:
        print d3.pop(),
    except IndexError:
        break
print
print '*' * 80
d4 = collections.deque(xrange(6))
while True:
    try:
        print d4.popleft(),
    except IndexError:
        break
print






