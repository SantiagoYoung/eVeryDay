
import multiprocessing
import sys
import time

def worker_with(lock, stream):
    with lock:
        time.sleep(5)
        stream.write('Lock acquired via with\n')

def worker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()

lock = multiprocessing.Lock()
w =multiprocessing.Process(target=worker_with, args=(lock, sys.stdout))

nw = multiprocessing.Process(target=worker_no_with, args=(lock, sys.stdout))

w.start()
nw.start()

w.join()
nw.join()


