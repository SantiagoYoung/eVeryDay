
import logging
import time
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


def lock_holder(lock):
    logging.debug('start')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(10)
        finally:
            logging.debug('Not holding.')
            lock.release()
        time.sleep(10)
    return


def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(5)
        logging.debug('Trying to acquire')

        have_it = lock.acquire(0)
        print have_it,'....'
        # print lock.acquire(1), '././...'

        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired',num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


lock = threading.Lock()
holder = threading.Thread(target=lock_holder, args=(lock,), name='LockHolder')
holder.setDaemon(True)
holder.start()

worker = threading.Thread(target=worker, args=(lock,), name='Worker')
worker.start()














