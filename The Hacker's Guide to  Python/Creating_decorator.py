

#
# def identity(f):
#     print 'hello'
#     return f
#
# @identity
# def foo():
#     print 'bar'


_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    print 'o'
    return f

@register
def nb():
    return 'bar'

# print nb
# print nb()
# print _functions
# print nb().__name__, '1'

# print nb.__name__





class Store(object):
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception('no')
        return self.storage.get(food)
    def put_food(self, username, food):
        if username != 'admin':
            raise Exception('nonono')
        self.storage.put(food)

# refactor checking func
def check_id_admin(username):
    if username != 'admin':
        raise Exception('nono')



def check_is_admin(f):
    def _check(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('nono')
        return f(*args, **kwargs)
    return _check






























