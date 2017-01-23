
import collections

d = collections.deque(xrange(10))
print 'Normal  :', d

d = collections.deque(xrange(10))
d.rotate(2)
print 'Right rotation:', d

d = collections.deque(xrange(10))
d.rotate(-2)
print 'Left rotation:', d

