
import copy


class MyClass(object):

    def __init__(self, name):
        self.name = name

    def __cmp__(self, other):
        return cmp(self.name, other.name)


a = MyClass('a')
my_list = [ a ]
dup = copy.deepcopy(my_list)


print '    mylist:', my_list
print '    dup:', dup
print '    dup is my_list:', (dup is my_list)
print '    dup == my_list:', (dup == my_list)
print '    dup[0] is my_list[0]:', (dup[0] is my_list[0])
print '    dup[0] == my_list[0]:', (dup[0] == my_list[0])
