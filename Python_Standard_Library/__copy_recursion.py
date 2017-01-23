


import copy
import pprint


class Graph(object):

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections


    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name=%s, id=%s)' % (self.name, id(self))

    def __deepcopy__(self, memo):
        print '\nCalling __deepcopy__ for %r' % self
        if self in memo:
            existing = memo.get(self)
            print ' Already copied to %r ' % existing
            return existing
        print ' Memo Dictionary:'
        pprint.pprint(memo, indent=4, width=40)

        dup =Graph(copy.deepcopy(self.name, memo), [])

        print 'Copying to new object %s' % dup
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup


root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.add_connection(a)
root.add_connection(b)

dup = copy.deepcopy(root)




