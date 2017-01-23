
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

def consumer(condition):
    logging.debug("Starting consumer thread.")
    t = threading.currentThread()
    with condition:
        condition.wait()
        logging.debug('Resource is available to consumer.')

def producer(condition):
    logging.debug('Starting producer thread')
    with condition:
        logging.debug('Making resource available')
        condition.notifyAll()

condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(10)
c2.start()
time.sleep(10)
p.start()

