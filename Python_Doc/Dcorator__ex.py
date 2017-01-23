








def decorator_with_arg(func):
    def _wrapper(arg1, arg2):
        print '{}:{}'.format(arg1, arg2)
        return func(arg1, arg2)
    return _wrapper

@decorator_with_arg
def print_name(f_name, l_name):
    print 'name {} {}'.format(f_name, l_name)
    return 0

print print_name('u', 'v')



# if __name__ == '__main___':
#     print print_name('u', 'v')

def my_deco(f):
    print 'i am func'
    def wrapper():
        print 'i am func dec'
        f()
    return wrapper
def lazy_func():
    print 'zzz'
# de_func = my_deco(lazy_func)

@my_deco
def u():
    print 'uuuuu'




print '-' * 50
def maker():
    print 'i make dec!'

    def my_dec(f):
        print 'i am dec'

        def _wrapper():
            print 'i am wrapper.'
            return f()
        print 'i return wrapped func'
        return _wrapper

    print 'i return deco'
    return my_dec


new_decorator = maker()
print new_decorator, 'neon'

print '-'*60

def dec_func():
    print 'i am dec func.'
print new_decorator(dec_func)

def deco_func():
    print 'i am the decorated func.'

print '*'*60
deco = maker()(deco_func)
print deco

print '%' * 70
print deco()

print '&' * 60
@maker()
def deco_func():
    print 'i am the dec'

print deco_func
print deco_func()
