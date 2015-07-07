#!/usr/bin/env python

__author__ = 'Shaun Rong'
__version__ = '0.1'
__maintainer__ = 'Shaun Rong'
__email__ = 'rongzq08@gmail.com'


def count_inversion(a, n):
    if n == 1:
        return a, 0
    else:
        l = a[0:int(n/2)]
        r = a[int(n/2):]
        (b, x) = count_inversion(l, int(n/2))
        (c, y) = count_inversion(r, n - int(n/2))
        (d, z) = count_split_inversions(b, c, n)
        return d, x + y + z


def count_split_inversions(l, r, n):
    i = j = z = 0
    d = []
    for k in range(n):
        if i >= len(l) and j >= len(r):
            print i, len(l)
            print j, len(r)
            print n
            print k
            print d
            print l, r
            raise IndexError('list index out of range')
        if i >= len(l) and j < len(r):
            d.append(r[j])
            j += 1
        if j >= len(r) and i < len(l):
            d.append(l[i])
            i += 1
        if i < len(l) and j < len(r):
            if l[i] < r[j]:
                d.append(l[i])
                i += 1
            else:
                d.append(r[j])
                j += 1
                z += len(l) - i

    return d, z

if __name__ == '__main__':
    with open('IntegerArray.txt', 'r') as f:
        data = f.readlines()
    a = []
    for x in data:
        a.append(int(x.strip()))
    d, z = count_inversion(a, len(a))
    print z
    #print len(a[0:int(len(a)/2)]) + len(a[int(len(a)/2): ])