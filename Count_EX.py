# -*- coding: utf-8 _8_


from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
print word_counts
top_three= word_counts.most_common(3)
print top_three

# 讨论
# 作为输入， Counter 对象可以接受任意的由可哈希(hashable)元素构成的序列对象。
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。比如：

print word_counts['eyes']

morewords = ['why','are','you','not','looking','in','my','eyes']

# 或者你可以使用 update() 方法：
word_counts.update(morewords)
print word_counts


# Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。比如：


a = Counter(words)
b = Counter(morewords)

print a
print b

c = a + b
print c
d = a - b
print d




































