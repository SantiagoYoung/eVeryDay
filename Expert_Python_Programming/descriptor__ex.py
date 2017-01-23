




class UpperString(object):
    def __init__(self):
        self._value = 'banana'
    def __get__(self, instance, klass):
        return self._value
    def __set__(self, instance, value):
        self._value = value.upper()


class MyClass(object):
    attribute = UpperString()

instance_of = MyClass()
print instance_of.attribute

instance_of.attribute = 'u check now'
print instance_of.attribute

print instance_of.__dict__
instance_of.new_attr = 'new'

print instance_of.__dict__
print '*' * 80

MyClass.new_attr = UpperString()
print instance_of.__dict__
print instance_of.new_attr
instance_of.new_attr = 'other '
print instance_of.new_attr
print instance_of.__dict__
print '&' * 87
class Whatever(object):
    def __get__(self, instance, klass):
        return 'whatever'

MyClass.whatever = Whatever()
print instance_of.__dict__
print instance_of.whatever
instance_of.whatever = 1
print instance_of.__dict__






