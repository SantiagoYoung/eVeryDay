#-8- coding: utf-8 -8-

# 1.11 命名切片

###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

print cost

# 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。比如：

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print items[a]
# 如果你有一个切片对象a，
# 你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息。比如：
a = slice(5,  50, 2)
print a.start
print a.stop
print a.step
# 另外，你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上，
# 这个方法返回一个三元组 (start, stop, step) ，
# 所有值都会被合适的缩小以满足边界限制，
# 从而使用的时候避免出现 IndexError 异常。比如：
s = 'HelloWorld'
print a.indices(len(s))
for i in range(*a.indices(len(s))):
    print s[i],
