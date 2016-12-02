#!/usr/bin/env python

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/gp/'
ISBNs ={
    '013269937':'Core Python Programming',
    '0132356139':'Python Web Development With Django',
    '0137143419':'Python Fundamentals',
}
def get_ranking(isbn):
    page = urlopen('%s%s'%(AMZN, isbn))
    # page = urlopen('https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3')
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]
def _show_ranking(isbn):
    print '- %r ranked %s' %(ISBNs[isbn], get_ranking(isbn))

def main():
    for isbn in ISBNs:
        _show_ranking(isbn)

@register
def _atexit():
    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
