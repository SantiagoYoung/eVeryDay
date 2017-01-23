
class DistinctError(Exception):
    pass

class DistinctDict(dict):

    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)
            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DistinctError('already exsit %s' % str(self[existing_key]))
        except ValueError:
            pass
        super(DistinctDict, self).__setitem__(key, value)

my = DistinctDict()

my['key'] = 'value'
print my['key']
# my['key2'] = 'value'




class folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self):
        print 'i am %s' % self.name
        for element in self:
            print element
fold = folder('neno')
fold.append('pics')
fold.append('video')
print fold.dir()







































































