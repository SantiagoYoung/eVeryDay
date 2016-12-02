import itertools



def starting_at_five():
    value = raw_input().strip()
    while value != '':
        for i in itertools.islice(value.split(), 4, None):
            yield i
        value = raw_input().strip()


def with_head(iterable, headsize=1):
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)), b

print with_head('abc')
print with_head('abcdefg', 4)

def compress(data):
    return ( (len(list(group)), name) for name, group in itertools.groupby(data))
def decompress(data):
    return (car * size for size, car in data)

print list(compress('get uuuuuuuup'))

compressed = compress('get upppppppppppppppp')
print ''.join(decompress(compressed))