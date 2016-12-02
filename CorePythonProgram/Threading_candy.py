#!/usr/bin/env python
from atexit import register
from threading import Thread, Lock, BoundedSemaphore
from random import randrange
from time import ctime, sleep

lock = Lock()
MAX = 5
candystary = BoundedSemaphore(MAX)


# class MyBoundedSemaphore(BoundedSemaphore):
#     # def __init__(self):
#     #     super(MyBoundedSemaphore, self).__init__()
#
#     def __len__(self):
#         return len(self)
# a = MyBoundedSemaphore(3)
# print len(a)



def refill():

    lock.acquire()
    print 'Refilling candy...'
    try:
        candystary.release()
    except ValueError:
        print 'full, skipping.'
    else:
        print 'ok.'
    lock.release()

def buy():

    lock.acquire()
    print 'Buying candy...'
    if candystary.acquire(False):
        print 'ok .'
    else:
        print 'empty, skipping'
    lock.release()

def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))
def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))

def _main():
    print 'starting at:', ctime()
    nloops = randrange(2, 6)
    print 'The candy machine (full with %d bars)!' % MAX
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print 'all Done at:', ctime()

if __name__ == '__main__':
    _main()





