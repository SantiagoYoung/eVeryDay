
from itertools import *

import operator
import pprint







class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)
    def __cmp__(self, other):
        return cmp((self.x, self.y), (other.x, other.y))


data = list(imap(Point, cycle(islice(count(), 3)),
                 islice(count(), 7),))
print 'Data:',
pprint.pprint(data, width=69)
print

print 'Group, unsorted:'
for k, g in groupby(data, operator.attrgetter('x')):
    print k, list(g)
print



data.sort()
print 'Sorted:'
pprint.pprint(data, width=69)
print


print 'Group, sorted:'
for k, g in groupby(data, operator.attrgetter('x')):
    print k, list(g)
print


