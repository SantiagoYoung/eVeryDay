
import bisect

class SortedList(list):

    def __init__(self, iterable):
        super(SortedList, self).__init__(sorted(iterable))

    def insort(self, item):
        bisect.insort(self, item)

    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop], value)
        if start:
            place += start
        end = stop or len(self)
        if place < end and self[place] == value:
            return place
        raise ValueError('%s not in list' % value)

so = SortedList([1, 2, 3])
so.insort(4)
print so.index(3)
# so.index(5)
