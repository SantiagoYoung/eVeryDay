import os
from random import randrange



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

def connect(db):
    global DB_EXC
    dbDir = '%s_%s' % (db, DBNAME)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect((os.path.join(dbDir, DBNAME)))
    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC
        except ImportError:
            return None

        try:
            cxn = MySQLdb.connect(user='root', passwd='yinxianjun',db=DBNAME)
        except DB_EXC.OperationalError:
            try:
                cxn = MySQLdb.connect(user='root', passwd='yinxianjun',db=DBNAME)
                cxn.query('CREATE DATABASE %s' % DBNAME)
                cxn.commit()
                cxn.close()
                cxn = MySQLdb.connect(user='root', passwd='yinxianjun',db=DBNAME)
            except DB_EXC.OperationalError:
                return None

    def create(cur):
        try:
            cur.execute(''' CREATE TABLE users(
            login VARCHAR(%d),
            userid INTEGER,
            projid INTEGER
            ''' %  NAMELENE)
        except DB_EXC.OperationalError:
            cur.drop(cur)
            create(cur)
            

