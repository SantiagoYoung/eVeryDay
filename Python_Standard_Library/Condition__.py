
import time
import threading


def consumer(condition):
    t = threading.currentThread()
    with condition:
        condition.wait()
        print '{}: Resource is available to consumer'.format(t.name)


def producer(condition):
    t = threading.currentThread()
    with condition:
        print '{}: Making resource available'.format(t.name)
        condition.notifyAll()

condition = threading.Condition()


c1 = threading.Thread(target=consumer, args=(condition,))
c2 = threading.Thread(target=consumer, args=(condition,))

p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()
