from fnmatch import *


def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a


for x in range(0, 10 ** 5):
    if fnmatch(str(x ** 2), '1?2*0*2?1'):
        m = f(x)
        if len(m) == 2:
            print(x ** 2)
