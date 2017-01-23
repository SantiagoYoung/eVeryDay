
from __future__ import with_statement

hosts = file('/etc/hosts')
try:
    for line in hosts:
        if line.startswith('#'):
            continue
        # print line
finally:
    hosts.close()

with file('/etc/hosts') as hosts:
    for line in hosts:
        if line.startswith('#'):
            continue
        # print line

class Context(object):
    def __enter__(self):
        print 'entering '
    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'leaving '
        if exc_type is None:
            print 'with no error'
        else:
            print 'with error %s' % exc_val

from contextlib import contextmanager
@contextmanager
def context():
    print 'entering'
    try:
        yield
    except Exception, e:
        print 'with an error %s' % e
        raise e
    else:
        print 'with no error'

@contextmanager
def logged(klass, logger):
    def _log(f):
        def __log(*args, **kwargs):
            logger(f, args, kwargs)
            return f(*args, **kwargs)
        return __log

    for attribute in dir(klass):
        if attribute.startswith('_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, '__logged_%s' % attribute, element)
        setattr(klass, attribute, _log(element))
    yield klass
    for attribute in dir(klass):
        if not attribute.startswith('__logged_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, attribute[len('__logged_'):], element)
        delattr(klass, attribute)

class One(object):
    def _private(self):
        pass
    def one(self, other):
        self.two()
        other.thing(self)
        self._private()
    def two(self):
        pass
class Two(object):
    def thing(self, other):
        other.two()
calls = []
def called(meth, args, kw):
    calls.append(meth.im_func.func_name)

if __name__ == '__main__':
    # with Context():
    #     print 'i am u zone'
    #     try:
    #         raise TypeError('i am the bug')
    #     except:
    #         print 'ex'
    #     finally:
    #         print 'd'
    a = context()
    with logged(One, called):
        one = One()
        two = Two()
        one.one(two)
    print calls



















