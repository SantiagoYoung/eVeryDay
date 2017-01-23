


import threading


def worker(i):
    '''thread worker function'''
    print ' %s  :Worker' % i
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,) )
    threads.append(t)
    t.start()






