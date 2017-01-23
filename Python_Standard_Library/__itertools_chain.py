
from itertools import *


for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print i

print

for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
print


print 'Stop at 5:'
for i in islice(count(), 5):
    print i,
print '\n'

print 'Start at 5, Stop at 10:'
for i in islice(count(), 5, 10):
    print i,
print '\n'

print 'By tens to 100:'
for i in islice(count(), 0, 100, 1):
    print i,
print '\n'


