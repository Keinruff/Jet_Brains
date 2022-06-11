
# # section 1
#
#
# from sys import argv
#
#
# def zp(time, s, p):
#     rez = (time * s) + p
#     return rez
#
#
# a1, a2, a3 = map(int, argv[1:])
#
# print('section 1: ', zp(a1, a2, a3))


# section 2

li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [li[i] for i in range(len(li)) if li[i] > li[i-1]]
print('section 2: ', new)


# section 3


print('section 3: ', [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])


# section 4

li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in set(li) if li.count(el) == 1]
new2 = [li[i] for i in range(len(li)) if li.count(li[i]) == 1]
print('section 4: ', new)
print('section 4: ', new2)


# section 5

from functools import reduce


li = [i for i in range(100, 1001) if i % 2 == 0]
new = reduce(lambda x, y: x * y, li)
print('section 5: ', new)


# section 6


from itertools import count
print('section 6: ')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('*' * 50)

from itertools import cycle
i = 0
li = [2, 7, 23, 1, 44]
fl = []
for el in cycle(li):
    if i > 10:
        break
    print(el)
    fl.append(el)
    i += 1
print(fl)

# section 7

n = 5




