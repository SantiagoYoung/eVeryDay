#!/usr/bin/env python

import nntplib
import socket

HOST ='your.nntp.server'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = 'uuu'

def main():

    try:
        n = nntplib.NNTP(HOST,
        user = USER,
        password = PASS)
    except socket.gaierror as e:
        print 'error: '
        return

    except nntplib.NNTPPermanentError as e:
        print 'error: '
        return

    print 'connected..'

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPPermanentError as ee:
        print 'error,,,'

        n.quit()
        return
    except nntplib.NNTPTemporaryError as ee:
        print 'errr;;'
        n.quit()
        return
    print '>>> found newsgroup '


    rng = lst, lst
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subj', rng)
    rsp, dat = n.xhdr('date', rng)
    print '..found last article'

    rsp, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):

    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True

    for line in lines:
        if line:
            lower = line.lower()
            if line.startswith('>')