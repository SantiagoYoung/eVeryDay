#!/usr/bin/env python


def gen_func():
    yield 5566
print gen_func
print gen_func()

g = gen_func()
print next(g)
# print next(g)

g = (_ for _ in range(2))
print g.next()
print g.next()
# print g.next()

def prime(n):
    p = 2
    while n > 0:
        for _ in range(2,p):
            if p % _ == 0:
                break
        else:
            yield p
            n -= 1
        p += 1
p = prime(4)
print next(p)
print next(p)
print next(p)





class Count(object):
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        n = self._n
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        n = 1
        while n <= self._n:
            yield n
            n += 1
for _ in Count(5):
    print _,
for _ in reversed(Count(5)):
    print _,


def spam():
    msg = yield
    print 'message', msg

try:
    g = spam()
    print next(g)

    g.send('hello world')

except StopIteration:
    pass





def subgen():
    try:
        yield 9527

    except ValueError:
        print 'get value error'
#
# def delegating_gen():
#     yield from subgen()
# g = delegating_gen()
try:
    next(g)
    g.throw(ValueError)
except StopIteration:
    print 'gen stop'




def average():
    total = 0
    count = 0
    avg = None
    while True:
        val= yield
        if not val:
            break
        total += val
        count += 1
        avg = total / count
    yield avg
g = average()
next(g)
g.send(3)
g.send(5)
print next(g)
# print next(g)
try:
    g.send(None)
except StopIteration as e:
    # ret = e.value
    pass
# print ret

def chain():
    for _ in 'ab':
        yield _
    for _ in range(3):
        yield _

a = chain()
print a
b = list(a)
print b




def sg():
    for _ in range(3):
        yield _

EXP = sg()
def delegateing_gen():
    _i = iter(EXP)
    try:
        _y = next(_i)
    except StopIteration , _e:
        RES = _e.value
    else:
        while True:
            _s = yield _y
            try:
                _y = _i.send(_s)
            except StopIteration as _e:
                REs = _e.value
                break
g = delegateing_gen()
print next(g)
print next(g)















