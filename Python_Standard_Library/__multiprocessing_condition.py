


import multiprocessing
import time


def stage_1(condition):

    name = multiprocessing.current_process().name

    print 'Starting:', name
    with condition:
        print '%s done and ready for stage 2' % name
        time.sleep(4)
        condition.notify_all()

def stage_2(condition):

    name = multiprocessing.current_process().name
    print 'Starting', name
    with condition:
        condition.wait()
        print '%s running' % name

if __name__ == '__main__':

    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name='s1', target=stage_1, args=(condition,))

    s2_clients = [ multiprocessing.Process(name='stage_2[%d]' % i, target=stage_2, args=(condition,)) for i in range(1, 3)]

    for c in s2_clients:
        c.start()
        time.sleep(1)

    s1.start()
    s1.join()

    for c in s2_clients:
        c.join()

