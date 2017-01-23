
import logging
import threading
import random


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet.')
    else:
        logging.debug('value=%s', val)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):
    def __init__(self, value):
        logging.debug('Inittializing %r', self)
        self.value = value

local_data =MyLocal(1000)
show_value(local_data)


for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()














