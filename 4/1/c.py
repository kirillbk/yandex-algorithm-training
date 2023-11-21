# C. Слияние

def merge(
        a: list,
        l: int,
        m: int,
        r: int,
        res: list,
        i: int
    ):
    it1 = l
    it2 = m

    while it1 < m and it2 < r:
        if a[it2] < a[it1]:
            res[i] = a[it2]
            it2 += 1
        else:
            res[i] = a[it1]
            it1 += 1
        i += 1

    while it1 < m:
        res[i] = a[it1]
        it1 += 1
        i += 1
    while it2 < r:
        res[i] = a[it2]
        it2 += 1
        i += 1


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = [0] * (n + m)
merge(a + b, 0, n, n + m, result, 0)
print(*result)
