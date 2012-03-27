from timeit import Timer
from io import BytesIO

def f():
    s = ''
    for i in xrange(1000):
        s += '1234567890'

def g():
    a = []
    for i in xrange(1000):
        a.append('1234567890')
    s = ''.join(a)

def h():
    b = BytesIO()
    for i in xrange(1000):
        b.write('123456')
    s = b.getvalue()

print Timer('f()', 'from __main__ import f').timeit(10000)
print Timer('g()', 'from __main__ import g').timeit(10000)
print Timer('h()', 'from __main__ import h').timeit(10000)
