# B. Быстрая сортировка

from random import randrange


def partition(a: list, l: int, r, x: int) -> (int, int):
    e = g = l

    for n in range(l, r):
        y = a[n]
        if y < x:
            a[n] = a[g]
            a[g] = a[e]
            a[e] = y
            e += 1
            g += 1
        elif y == x:
            a[n] = a[g]
            a[g] = y
            g += 1

    return e, g


def _qsort(a: list, l: int, r: int):
    if r - l > 1:
        pivot = a[randrange(l, r)]
        e, g = partition(a, l, r, pivot)
        _qsort(a, l, e)
        _qsort(a, g, r)


def quick_sort(a: list, n: int):
    _qsort(a, 0, n)


n = int(input())
a = list(map(int, input().split()))
quick_sort(a, n)
print(*a)
