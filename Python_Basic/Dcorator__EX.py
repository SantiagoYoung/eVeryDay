
def makebold(fn):
    def _wrapper():
        return '<b>' + fn() + '<b>'
    return _wrapper

def makeitalic(fn):
    def _wrapper():
        return '<i>' + fn() + '<i>'
    return _wrapper


@makebold
@makeitalic
def hello():
    return 'hello world.'
print hello()

# Decorator Basics
#
'''
functios are objects in Python.
'''
def shout(word='yes'):
    return word.capitalize()
print shout()
# as an object, u can assign the function to a variable
# like any other object.
scream = shout
print scream()
del shout
try:
    print shout()
except NameError, e:
    print e
print scream()


def talk():

    def whisper(word='yes'):
        return word.lower() + '....'

    print whisper()


talk()

try:
    print whisper()
except NameError, e:
    print e

# Functions references

'''
functions are objects,
Therefore, functions:
    can be assigned to a vatiable.
    can be defined in another function.
'''
# a function can return another function.

def getTalk(kind='shout'):

    def shout(word='yes'):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower() + '....'

    if kind == 'shout':
        return shout
    else:
        return whisper


talk = getTalk()
print talk
print talk()

print getTalk('whisper')()


# if u can return a function, u can pass one as a parameter

def doSomethingBefore(func):
    print 'i do something before then i call the function u give me '
    print func()

doSomethingBefore(scream)

'''
decorators are "wrappers", which means that
they let u execute code before and after the
function they decorate without modifying the
fuction itself.
'''

# Handcrafted decorators

# a decorator is a function that expects
# ANOTHER function as parameter
def my_decorator(func):

    def wrapper():
        print 'before the code u want to execute.'
        func()
        print 'after the function runs.'

    return wrapper
    # return wrapper()

def a_func():
    print 'i am a stand alone function.'

print '>>>', my_decorator(a_func)


# Decorators demystified


@my_decorator
def b_func():
    print 'leave me alone.'

print '>>>', b_func()
print b_func




def bread(func):
    def wrapper():
        print '</*****\>'
        func()
        print "<\____/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print '#tomatoes#'
        func()
        print "~salad~"
    return wrapper

def sandwich(food='--ham--'):
    print food

# print sandwich()
# print bread(sandwich)()
# print ingredients(sandwich)()

@bread
@ingredients
def sandwich(food='--ham--'):
    print food

# sandwich()

# Taking decorators to the next level
#
# Passing arguments to the decorated function

def a_decorator(func):
    def a_wrapper(a1, a2):
        print 'i got : {}, {}'.format(a1, a2)
        func(a1, a2)
    return a_wrapper

@a_decorator
def pname(a1, a2):
    print 'my name is {} {}'.format(a1, a2)

pname('he', 'yoo')

# Decorating methods
'''
# One nifty thing about Python is that methods and
# functions are really the same. The only difference is
# that methods expect that their first argument is
# a reference to the current object (self).
'''

def c_decorator(func):
    def wrapper(self, lie):
        lie = lie - 3
        return func(self, lie)
    return wrapper

class Lucy(object):

    def __init__(self):
        self.age  = 32

    @c_decorator
    def yo(self, lie):
        print 'i am {0}, what did u think?'.format(self.age + lie)

l = Lucy()
l.yo(-1)

# Passing arguments to the decorator




def decorator_maker():

    print 'i make decorators, ' \
          'i am execute once.'

    def my_decorator(func):
        print 'i am a decorator.'

        def wrapper():
            print 'i am the wrapper aroud the func.'
            return func

        return wrapper

    print 'i return the decorator.'
    return my_decorator

new_decorator = decorator_maker()
print type(new_decorator)

def de_func():
    print 'i am the deco func'

u = new_decorator(de_func)
print type(u)
u()
print type(u())
u()()



































