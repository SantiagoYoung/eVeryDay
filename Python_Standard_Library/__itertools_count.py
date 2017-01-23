

from itertools import *



for i in izip(count(1), ['a','b', 'c']):
    print i

print '****' * 10


for  i, item in izip(xrange(7), cycle(['a', 'b', 'c','d'])):
    print (i, item)


print '****' * 10


for i in repeat('over-and-over', 5):
    print i


print '****' * 10


for i, s in izip(count(), repeat('uuu', 5)):
    print i, s

print '****' * 10



for i in imap(lambda x, y:(x, y, x*y), repeat(2), xrange(5)):
    print '%d * %d = %d' % i















