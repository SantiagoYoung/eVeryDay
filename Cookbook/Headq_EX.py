from heapq import nlargest, nsmallest

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print nlargest(2, nums)
print nsmallest(2, nums)


porfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 454.123},
    {'name': 'FB', 'shares': 200, 'price': 23.1},
    {'name': 'HP', 'shares': 34, 'price': 12.2},
    {'name': 'Yahho', 'shares': 23, 'price': 123.123},
    {'name': 'ACM', 'shares': 78, 'price': 114.123}
]

cheap = nsmallest(2, porfolio, key=lambda x: x['price'])
expensive = nlargest(2, porfolio, key=lambda x: x['price'])

print cheap
print expensive






import heapq

class PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)



q  = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print q._queue

print q.pop()
print q.pop()
print q.pop()
print q.pop()






















