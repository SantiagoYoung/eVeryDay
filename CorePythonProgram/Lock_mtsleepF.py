from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import ctime, sleep


class CleanOutSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2,5) for x in xrange(randrange(3,7)))
remaining = CleanOutSet()
lock = Lock()

def loop(nsec):
    myname = current_thread().name

    # lock.acquire()
    # remaining.add(myname)
    # print '[%s] Started %s' %(ctime(), myname),'gogogogo'
    # lock.release()
    with lock:
        remaining.add(myname)
        print '[%s] Started %s' % (ctime(), myname), 'gogogogo'

    sleep(nsec)

    # lock.acquire()
    # remaining.remove(myname)
    # print '[%s] Completed %s (%d secs)' %(
    #     ctime(), myname, nsec
    # )
    # print ' (remaining: %s)' % (remaining or 'None')
    # lock.release()
    with lock:
        remaining.remove(myname)
        print '[%s] Completed %s (%d secs)' % (
            ctime(), myname, nsec
        )
        print ' (remaining: %s)' % (remaining or 'None')


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexist():
    print 'all done at:', ctime()

if __name__ == '__main__':
    _main()