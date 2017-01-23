
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print ' i make decorators! And i accept arguments: {}, {}'.format(decorator_arg1, decorator_arg2)

    def my_decorator(f):

        print ' i am decorator. Somehow u pass me arguments: {0}, {1}'.format(decorator_arg1, decorator_arg2)

        def wrapper(func_arg1, func_arg2):
            print ''' i am the wrapper aroud the decorated func.\n'\
                    'i can access all the variables \n' \
                    '\t- from the decorator: {0} {1}\n'\
                    '\t- from the func call: {2} {3}\n'\
                    'then i pass then to the decorated function.'''\
                    .format(decorator_arg1, decorator_arg2,
                            func_arg1, func_arg2)

            return f(func_arg1, func_arg2)
            # return f(decorator_arg1, decorator_arg2)
        return wrapper
    return my_decorator

@decorator_maker_with_arguments('leonard', 'sheldon')
def decorated_func_with_arguments(fun_arg1, fun_arg2):
    print 'i am the decorated function and only knows about my arguments:{0},{1}'.format(fun_arg1, fun_arg2)

print decorated_func_with_arguments('neon', 'viber')
#                                                    But remember decorators are called only once.


print '-'*70

def decorator_with_args(decorator_to_enance):

    def decorator_maker(*args, **kwargs):

        def decorator_wrapper(f):

            return decorator_to_enance(f, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker

@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(func_arg1, func_arg2):
        print 'deco {0} {1}'.format(func_arg1, func_arg2)
        return func(func_arg1, func_arg2)
    return wrapper

@decorated_decorator(42, 404, 1024)
def deco_func(fuc_arg1, fuc_arg2):
    print 'hello {0} {1}'.format(fuc_arg1, fuc_arg2)

print deco_func('Universe and ', 'everything')

















