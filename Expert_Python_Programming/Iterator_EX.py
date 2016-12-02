



class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        ''' return the next element'''
        if self.step == 0:
            # print 'hello'
            raise StopIteration
            # raise StandardError
        self.step -= 1
        return self.step

    def __iter__(self):
        ''' return the iterator itself'''
        return self

my = MyIterator(4)
# print my.next()
# print my.next()
# print my.next()
# print my.next()
# print my.next()


for i in MyIterator(4):
    print i



def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

fib = fibonacci()
print [ fib.next() for i in range(10) ]




def power(values):
    for value in values:
        print 'powering %s ' % value
        yield value

def adder(values):
    for value in values:
        print 'adding to %s ' % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2
elements = [1, 4, 7, 9, 12, 19]
res = adder(power(elements))
print res.next()
print res.next()
print res.next()
print res.next()
print res.next()























