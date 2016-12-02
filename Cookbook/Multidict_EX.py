# -8- coding: utf-8 -*-


# 1.6 字典中的键映射多个值

# 解决方案
# 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，
# 那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。
# 比如，你可以像下面这样构造这样的字典：
#
# d = {
#     'a' : [1, 2, 3],
#     'b' : [4, 5]
# }
# e = {
#     'a' : {1, 2, 3},
#     'b' : {4, 5}
# }


'''你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
 defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，
 所以你只需要关注添加元素操作了。比如：'''
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(1)

c = defaultdict(set)
c['a'].add(1)
c['a'].add(2)
c['a'].add(3)

print d, c

# 需要注意的是， defaultdict 会自动为将要访问的键(就算目前字典中并不存在这样的键)创建映射实体。
# 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
# 但是很多程序员觉得 setdefault() 用起来有点别扭。
# 因为每次调用都得创建一个新的初始值的实例(例子程序中的空列表 [] )。

print d



# 1.7 字典排序

# 问题
# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

# 解决方案
# 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。
# 在迭代操作的时候它会保持元素被插入时的顺序，示例如下：

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print d
for key in d:
    print key, d[key]

# 讨论
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
# 每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。
# 对于一个已经存在的键的重复赋值不会改变键的顺序。
#
# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，
# 因为它内部维护着另外一个链表。
# 所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候
# (比如读取100,000行CSV数据到一个 OrderedDict 列表中去)，
# 那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。


# 1.8 字典的运算

prices = {
    'acme': 45.32,
    'aapl': 612.18,
    'ibm': 205.55,
    'hpq': 37.21,
    'fb': 12.03,
}
print zip(prices.values(), prices.keys())
min_price = min(zip(prices.values(), prices.keys()))
print min_price
max_price = max(zip(prices.values(), prices.keys()))
print max_price
price_sorted = sorted(zip(prices.values(), prices.keys()))
print price_sorted

# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 比如，下面的代码就会产生错误：
#
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

print max(prices)
print min(prices)


# 前面的 zip() 函数方案通过将字典”反转”为(值，键)元组序列来解决了上述问题。
# 当比较两个元组的时候，值会先进行比较，然后才是键。
# 这样的话你就能通过一条简单的语句就能很轻松的实现在字典上的求最值和排序操作了。
#
# 需要注意的是在计算操作中使用到了(值，键)对。
# 当多个实体拥有相同的值的时候，键会决定返回结果。
# 比如，在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回：

# >>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
# >>> min(zip(prices.values(), prices.keys()))
# (45.23, 'AAA')
# >>> max(zip(prices.values(), prices.keys()))
# (45.23, 'ZZZ')
# >>>




# 1.9 查找两字典的相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}


# python3
print a.keys() & b.keys()
print a.keys() - b.keys()
print a.items() & b.items()

# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }
#
# 这些操作也可以用于修改或者过滤字典元素。
# 比如，假如你想以现有字典构造一个排除几个指定键的新字典。
# 下面利用字典推导来实现这样的需求：

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}












