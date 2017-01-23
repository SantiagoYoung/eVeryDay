

def makebold(func):
    def _wrapper():
        return '<b>' + func() + "</b>"
    return _wrapper

def makeitalic(func):
    def _wrapper(*args, **kwargs):


        print 'sdf'
        print '::::{}:::{}:::'.format(args, kwargs)
        print  '<i>' + func(*args, **kwargs) + '</i>'

        print 'sdfsdfsdf'
        return
    return _wrapper

@makebold
@makeitalic
def hello():
    return 'hello world.'

@makeitalic
def h(arg1, arg2):
    return 'u'
a = hello
b = h

print a
print b('viber', 'neon')







def dec_maker():
    print 'i am maker.'

    def _decorator(func):
        print 'i am decrator.'

        def _wrapper():
            print 'I am wrapper.'
            return func()

        print 'I return the wrapper'
        return _wrapper
    print 'I return the dec'
    return _decorator

@dec_maker()
def gg():
    return 'I am function'

print gg()

















