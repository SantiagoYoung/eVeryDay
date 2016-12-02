#!/usr/bin/env python

class MyClass(object):

    neon = 'neon'
    def __init__(self):
        self.name = 'god'

    def printf(self):
        print 'Neon God.'

a = MyClass()

print hasattr(a, 'name')
print hasattr(MyClass, 'neon')
print hasattr(a, 'printf')

print getattr(a, 'name')
print getattr(a, 'printf')()

setattr(MyClass, 'santiago', 'young')
print MyClass.santiago

print isinstance(a, MyClass)

print issubclass(MyClass, object)

print globals()


a = 10
def fun():
    print 'i am callable'

print callable(a),'1'
print callable(fun),'2'
print '*'*20
print callable(fun()),'3'


class God(object):
    pass

def fun():
    pass

god = God()
print god.__class__.__name__
print fun.__name__

print '_' * 20

class ClsA(object):
    def __new__(cls, args):
        print '__new__' + args
        return object.__new__(cls, args)
    def __init__(self, arg):
        print '__init__' +  arg

o = ClsA('Hello')
print '_'*20
class ClsB(object):
    def __new__(cls, arg):
        print '__new__' + arg
        return object
    def __init__(self, arg):
        print '__init__' + arg

O = ClsB('hello')






class YourClass(object):
    def __str__(self):
        return 'your __str__'
    def __repr__(self):
        return 'your __repr__'
print '*'*20
print YourClass, '1'
print YourClass(), '3'
print str(YourClass())


a = {'1': 1, '2': 2, '3': 3}
b = {'2': 2, '3': 3, '4': 4}



class EmuList(object):
    def __init__(self, list_):
        self._list = list_

    def __repr__(self):
        return 'EmuList: ' + repr(self._list)
    def append(self, item):
        self._list.append(item)
    def remove(self, item):
        self._list.remove(item)
    def __len__(self):
        return len(self._list)
    def __getitem__(self, sliced):
        return self._list[sliced]
    def __setitem__(self, sliced, val):
        self._list[sliced] = val
    def __delitem__(self, sliced):
        del self._list[sliced]
    def __contains__(self, item):
        return item in self._list
    def __iter__(self):
        return iter(self._list)


emul = EmuList(range(5))
print emul
print emul[1:3]
print emul[0:4:2]
print len(emul)
emul.append(5)
print emul
emul.remove(2)
print emul
emul[3] = 6
print emul
print 0 in emul



class EmuDict(object):
    def __init__(self, dict_):
        self._dict = dict_
    def __repr__(self):
        return 'EmuDict: ' + repr(self._dict)
    def __getitem__(self, key):
        return self._dict[key]
    def __setitem__(self, key, val):
        self._dict[key] = val
    def __delitem__(self, key):
        del self._dict[key]
    def __contains__(self, key):
        return key in self._dict
    def __iter__(self):
        return iter(self._dict.keys())

emud = EmuDict({"1":1, '2':2,'3': 3})
print emud
print emud['1']
emud['5'] = 5
print emud
del emud['2']
print emud
for _ in emud: print emud[_],
print  '1' in emud




def decor(func):
    def wrapper(*args, **kwargs):
        print 'wrapper'
        func()
        print '_______'
    return wrapper
@decor
def exmp():
    print 'hello'
print exmp()



def exmple(val):
    def decor(func):
        def wrapper(*args, **kwargs):
            print 'Val is {0}'.format(val)
            func()
        return wrapper
    return decor
@exmple(10)
def undecor():
    print 'this is undercor func'
print undecor()

####################################################
def fib(self, n):
    if n <= 2:
        return 1
    return fib(self, n-1) + fib(self, n-2)

Fib = type('Fib', (object,), {'val': 10, 'fib': fib})
f = Fib()
print f.val
print f.fib
print f.fib(9)


##########
class calobj(object):
    def ex(self):
        print 'i am callable'
    def __call__(self, *args, **kwargs):
        self.ex()
ex = calobj()
print ex
print ex.ex()



import socket

class Socket(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        self.sock = sock
        return self.sock

    def __exit__(self, *exc_info):
        if exc_info[0] is not None:
            import traceback
            traceback.print_exception(*exc_info)
        self.sock.close()
if __name__ == '__main__':
    host = 'localhost'
    port = 5566
    with Socket(host, port) as s:
        while True:
            conn, addr = s.accept()
            msg = conn.recv(1024)
            print msg
            conn.send(msg)
            conn.close()















































































































