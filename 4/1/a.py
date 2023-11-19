# A. Partition

def partition(a: list, l: int, r: int, x) -> int:
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

    return e


n = int(input())
a = list(map(int, input().split()))
x = int(input())

i = partition(a, 0, n, x)
print(i)
print(n - i)
