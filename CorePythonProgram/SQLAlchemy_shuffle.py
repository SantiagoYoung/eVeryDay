#!/usr/bin/env python
from distutils.log import warn as printf
from os.path import dirname
from random import randrange
from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELENE = 16

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)
def setup():
    return RDBMSs[raw_input('''
    Choose a database system:

    (M)ySQL
    (G)adfly
    (S)QLite

    Enter choice: ''').strip().lower()[0]]
NAMES = (
    ('AARON', 8312),('ANGELA', 7603), ('dave', 7309),
    ('davina', 7902),('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jin', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 7607),('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)
def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()