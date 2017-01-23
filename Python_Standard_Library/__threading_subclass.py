


import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s)  %(message)s',
)


class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        return


for i in range(5):
    t = MyThread()
    t.start()
    t.join()










