

import time
import threading
import random




TIMEOUT = 2

def consumer(event, l):
    t = threading.currentThread()
    while 1:
        event_is_set = event.wait(TIMEOUT)
        if event_is_set:
            try:
                integer = l.pop()
                print '{} popped from list by {}'.format(integer, t.name)

                event.clear()
            except IndexError:
                pass

def producer(event, l):
    t = threading.currentThread()
    while 1:
        integer = random.randint(10, 100)
        l.append(integer)
        print  '{} appended to list by {}'.format(integer, t.name)
        event.set()
        time.sleep(1)

event = threading.Event()
l = []

threads = []

for name in ('consumer1, consumer2'):
    t = threading.Thread(name=name, target=consumer, args=(event, l))
    t.start()
    threads.append(l)


p = threading.Thread(name='producer1', target=producer, args=(event, l))
p.start()
threads.append(p)



for t in threads:
    t.join()
