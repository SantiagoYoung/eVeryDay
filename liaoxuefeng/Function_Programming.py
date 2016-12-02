#   coding: utf-8



# Higher-order function
'''
variable can point to function.
'''
# 既然变量可以指向函数，
# 函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，
# 这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
f = lambda x: x + 1
print add(1, 2, f)


# map()函数接收两个参数，
# 一个是函数，
# 一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。

r = map(lambda x: x*x , [1, 2, 3, 4, 5, 6, 7, 8, 9])
print type(r)

yoo = map(str, [1, 2, 3, 4, 5])
print yoo


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

yooo = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print type(yooo)




def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s ))

print str2int('147')

# filter()也接收一个函数和一个序列。
# 和map()不同的是，
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。


yoooo = filter(lambda x: x % 2 ==1, [1, 2, 3, 4, 5, 6])
print type(yoooo)
print yoooo


bb  = [-12, 1, 3, 109, 23, 2]
print sorted(bb)
print sorted(bb, key=abs)

cc = ['bob', 'about', 'Zoo', 'Credit']
print  sorted(cc)
print sorted(cc, key=str.lower)



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print sorted(L, key=lambda x: x[0])
print sorted(L, key=lambda x: x[0], reverse=True)


def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
for i in count1():
    print i
    print i()


def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(4):
        fs.append(f(i))
    return fs

for i in count2():
    print i , '>>>>'
    print i(), '>>>'

from functools import partial

# 简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。









class Student(object):
    __slot__ = ('name', 'age')

s = Student()
s.name = 'yo'
s.age = 1
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


