







class Citizen(object):
    def __init__(self):
        self._message = 'good boy'

    # @property
    def _get_message(self):
        return self._message

    kane = property(_get_message)

# print Citizen().kane



class MeanElephant(object):
    def __init__(self):
        self._people_to_kill = []

    def is_slapped_on_the_butt_by(self, name):
        self._people_to_kill.append(name)
        print 'Ouch!'
    def revenge(self):
        print '10 years later...'
        for person in self._people_to_kill:
            print 'me kill %s' % person
joe = MeanElephant()
# print joe.is_slapped_on_the_butt_by('neon')
# print joe.is_slapped_on_the_butt_by('bill')
# print joe.revenge()


class Base(object):
    def __secret(self):
        print 'nonono'
    def public(self):
        self.__secret()
print Base().public()
# print Base().__secret
# print Base.__secret

# print dir(Base)
# print Base.__dict__

class Derived(Base):
    def __secret(self):
        print 'never'

# print Derived().public()



class weirdint(int):
    def __add__(self, other):
        return int.__add__(self, other)
    def __repr__(self):
        return ' s %s' % self

    def do_this(self):
        print 'this'
    def do_that(self):
        print 'that'

a = weirdint()
print a + 1

class DB(object):
    is_connected = False
    has_cache = False






def fuzzy_thing(**kwargs):
    if 'do_this' in kwargs:
        print 'y'
    if 'do_that' in kwargs:
        print 'o'
    print 'error'
print fuzzy_thing()
print fuzzy_thing(do_this=1)
print fuzzy_thing(do_that=2)






















