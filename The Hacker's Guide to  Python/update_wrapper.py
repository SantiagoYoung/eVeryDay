

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__',
                       '__doc__','__annotations__')
WRAPPER_UPDATES = ('__dict__', )

def update_wwrapper(wrapper, wrapped,
                    assigned = WRAPPER_ASSIGNMENTS,
                    updated = WRAPPER_UPDATES):
    wrapper.__wrapped__ = wrapped
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except:
            pass
        else:
            setattr(wrapped, attr, value)

    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

    return wrapper

import functools
import inspect



def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        print func_args
        if func_args.get('username') != 'admin':
            raise Exception('nono')
        return f(*args, **kwargs)
    return wrapper

@check_is_admin
def get_food(username, type='cho'):
    return type + 'monmon'

# print get_food('1')




import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredient(self):
        '''no'''

class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients(self):
        return None

print DietPizza().get_ingredient()






























