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

# print DietPizza().get_ingredient()

class BasePizza(object):

    __metaclass__ = abc.ABCMeta

    ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        '''return '''
        return cls.ingredients

print BasePizza().get_ingredients()
class P(BasePizza):
    pass
print P().get_ingredients()




class BasePizza(object):

    __metaclass__ = abc.ABCMeta

    ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        '''return '''
        return cls.ingredients
class BB(BasePizza):
    def get_ingredients(self):
        return [1] + super(BB, self).get_ingredients()
print BB().get_ingredients()

