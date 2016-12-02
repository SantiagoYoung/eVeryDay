# coding: utf-8


# 1.13 通过某个关键字排序一个字典列表

# 解决方案
# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
# 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_id = sorted(rows, key=itemgetter('uid'))

print rows_by_fname
print rows_by_id

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print rows_by_lfname

# 讨论
# 在上面例子中， rows 被传递给接受一个关键字参数的 sorted() 内置函数。
# 这个参数是 callable 类型，并且从 rows 中接受一个单一元素，然后返回被用来排序的值。
# itemgetter() 函数就是负责创建这个 callable 对象的。



































