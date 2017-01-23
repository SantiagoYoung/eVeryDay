


from itertools import *


def check_item(x):
    print 'Testing:', x
    return (x<1)

for i in ifilter(check_item, [-1, 0, 1, 3, -2]):
    print 'Yielding:', i



print '**'*20


for i in ifilterfalse(check_item, [-1, 0, 1, 2, -2]):
    print 'Yielding:', i