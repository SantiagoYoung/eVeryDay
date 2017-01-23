

import signal

'''
def myHand(num, frame):
    print 'received:', num


signal.signal(signal.SIGTSTP, myHand)
signal.pause()

print 'end '
'''

def myHand(signum, frame):
    print 'it is time'
    exit()


signal.signal(signal.SIGALRM, myHand)
signal.alarm(5)
while True:

    print 'not u'














