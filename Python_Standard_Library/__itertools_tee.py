
from itertools import *


r = islice(count(), 5)
i1, i2 = tee(r)

# print 'i1:', list(i1)
# print 'i2:', list(i2)




print 'r:',
# print list(r)
for i in r:
    print i,
    if i > 1:
        break
print
print 'i1:', list(i1)
print 'i2:', list(i2)


print 'Double:',
for i in imap(lambda x:2*x, xrange(5)):
    print i

print 'Multiples:'
for i in imap(lambda x, y: (x, y, x*y), xrange(5), xrange(5, 10)):
    print '%d * %d = %d' % i

print  '%' * 60

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4,9)]
for i in starmap(lambda x, y: (x, y, x*y), values):
    print '%d * %d = %d' % i


