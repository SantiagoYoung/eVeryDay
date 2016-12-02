

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s) ' % self.name

    __repr__ = __str__

print Student('michael')

s = Student('neon')


class Fib(object):
    def __init__(self):
        self.a , self.b = 0, 1

    def __iter__(self):
        return self

    # __next__(self)  python3
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):

        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# for i in Fib():
#     print i
f = Fib()


class U(object):

    def __init__(self):
        self.name = 'neon'

    def __getattr__(self, yo):
        if yo == 'u':
            return 1
        raise AttributeError('U object has no attribute %s' % yo)
uu = U()
print uu.name
print uu.u
# print uu.o


class Chain(object):

    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path,path ))

    def __str__(self):
        return self._path

    __repr__ = __str__

print Chain('/hello/world').status.user.timeline.list




class Y(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print 'my name is  %s' % self.name
y = Y('neon')
print y(1)

#  callable




from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))





def triangle(n):
    L1 = []
    for i in range(n):
        l =[]












