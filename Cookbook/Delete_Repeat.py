# -8- coding: utf-8 -8-


# 1.10 删除序列相同元素并保持顺序


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print list(dedupe(a))
#
# 这个方法仅仅在序列中元素为 hashable 的时候才管用。
# 如果你想消除元素不可哈希(比如 dict 类型)的序列中重复元素的话，
# 你需要将上述代码稍微改变一下，就像这样：

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield seen
            seen.add(val)
            print seen

a = [{'x': 1, 'y': 2}, {'x': 1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print list(dedupe2(a, key=lambda d: (d['x'],d['y'])))























