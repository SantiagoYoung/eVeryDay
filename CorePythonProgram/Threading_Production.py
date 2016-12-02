#!/usr/bin/env python


from random import randint
from time import sleep
from Queue import Queue
from MyThread import MyThread
from threading import Lock

lock = Lock()


def writeQ(queue):
    print 'producing object for Q...&&&',
    queue.put('xxx', 1)
    print 'size now: ', queue.qsize()

def readQ(queue):
    val = queue.get(1)
    print val,'>>>>>>'
    print 'consumed object from Q .. size now:::', queue.qsize()

def writer(queue, loops):

    lock.acquire()
    for i in range(loops):
        writeQ(queue)
        sleep(randint(2, 5))
    lock.release()

def reader(queue, loops):
    lock.acquire()
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))
    lock.release()

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:

        t = MyThread(funcs[i], (q, nloops),
                     funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'all Done'

if __name__ == '__main__':
    main()


