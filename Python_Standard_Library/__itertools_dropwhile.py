
from itertools import *


def should_drop(x):
    print 'Testing:', x
    return (x<1)

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print 'Yielding:', i

print '***'*20

def should_take(x):
    print 'Testing:', x
    return (x<2)

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print 'Yielding:', i
