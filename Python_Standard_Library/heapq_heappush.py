

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data



heap = []
print 'random:', data
print

# for n in data:
#     print 'add %3d:' % n
#     heapq.heappush(heap, n)
#     show_tree(heap)

heapq.heapify(data)
print data