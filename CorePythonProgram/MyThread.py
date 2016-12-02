#!/usr/bin/env python
import threading
from time import ctime, sleep

loops = (4, 2)

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def get_result(self):
        return self.res

    def run(self):
        print 'starting ', self.name, 'at: ' , ctime()
        self.res = self.func(*self.args)

        print self.name, 'finished at: ', ctime()
        # print self.res

