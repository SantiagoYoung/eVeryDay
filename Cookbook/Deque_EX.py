from collections import deque
from atexit import register

def main():
    a = deque(maxlen=3)
    a.append(1)
    a.append(2)
    print a

    b = deque()
    b.append(1)
    b.appendleft(2)
    b.append(3)
    b.append(4)
    c =  b.pop()
    d = b.popleft()
    print c
    print d
    print b

def _atexit():
    print 'well done'


if __name__ == '__main__':
    main()



