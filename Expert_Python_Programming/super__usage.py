


class A(object):
    def __init__(self):
        print 'A'
        super(A, self).__init__()
class B(object):
    def __init__(self):
        print 'B'
        super(B, self).__init__()

class C(A, B):
    def __init__(self):
        print 'C'
        A.__init__(self)
        B.__init__(self)

print 'MRO:', [x.__name__ for  x in C.__mro__]
print C()

from collections import deque
print deque.__mro__

import random
print random.Random.__mro__