#!/usr/bin/env python

from random import randrange, chice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in xrange(randrange(5, 11)):
	dtint = randrange(maxint)
	dtstr = ctime(dtint)
	llen = randrange(4, 8)
	
