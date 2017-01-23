

import multiprocessing

def producer(ns, event):

    # ns.value = 'This is the value.'
    ns.my_list.append('this is the value')

    event.set()

def consumer(ns, event):
    # try:
    #     value = ns.value
    # except Exception, err:
    #     print 'Before event, error:', str(err)
    # event.wait()
    print 'Before event:', ns.my_list
    event.wait()
    print 'After event:', ns.my_list

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()

    namespace.my_list = []

    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer,
                                args=(namespace, event))

    c = multiprocessing.Process(target=consumer,
                                args=(namespace, event))

    c.start()
    p.start()

    c.join()
    p.join()
