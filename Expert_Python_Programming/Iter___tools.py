import itertools

def starting_at_five():
    value = raw_input().strip()

    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        value = raw_input().strip()

def with_head(ite, headsize=1):
    a, b = itertools.tee(ite)
    c = itertools.islice(a, 3)
    return list(itertools.islice(a, 3)), b, c.next()

from itertools import groupby
def compress(data):
    return ((name, len(list(num))) for name, num in groupby(data))
def decompress(data):
    return (i * n for i, n in data)









if __name__ == '__main__':
    iter = starting_at_five()
    print with_head([1, 2, 3, 4])
    print list(compress('get uuuuuuuup'))
    print ''.join(decompress(compress('get uuuuuup')))
