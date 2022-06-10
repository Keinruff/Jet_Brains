

from sys import argv


def zp(time, s, p):
    rez = (time * s) + p
    return rez


a1, a2, a3 = map(int, argv[1:])

print(zp(a1, a2, a3))