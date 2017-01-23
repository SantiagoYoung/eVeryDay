
import time
import threading


value = 0
lock = threading.Lock()

def getlock(lock):
    global value
    with lock:
        new = value + 1
        time.sleep(0.001)
        value = new

threads = []

for i in range(100):
    t = threading.Thread(target=getlock, args=(lock,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

print value