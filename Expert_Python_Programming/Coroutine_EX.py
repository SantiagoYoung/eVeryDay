from __future__ import with_statement
from contextlib import closing
import socket
import multitask


def coroutine_1():
    for i in range(3):
        print 'c1,' + str(i)
        yield i

def coroutine_2():
    for i in range(3):
        print 'c2,' + str(i)
        yield i

multitask.add(coroutine_2())
multitask.add(coroutine_1())
multitask.run()