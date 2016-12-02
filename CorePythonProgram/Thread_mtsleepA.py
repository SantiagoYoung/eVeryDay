#!/usr/bin/env python
import thread
from time import ctime, sleep

def loop0():
    print 'Start loop 0 at: ', ctime()
    sleep(4)
    print 'loop 0 done at: ', ctime()

def loop1():
    print 'Start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at: ', ctime()


def main():
    print 'start at:>>>>>>>>', ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all DONE at: ', ctime()


if __name__ == '__main__':
    main()



