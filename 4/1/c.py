# C. Слияние

def merge(
        a: list,
        i: int,
        b: list,
        j: int,
        res: list,
        k: int
    ):

    while i < len(a) and j < len(b):
        if b[j] < a[i]:
            res[k] = b[j]
            j += 1
        else:
            res[k] = a[i]
            i += 1
        k += 1

    for j in range(j, len(b)):
        res[k] = b[j]
        k += 1
    for i in range(i, len(a)):
        res[k] = a[i]
        k += 1


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = [0] * (n + m)
merge(a, 0, b, 0, result, 0)
print(*result)
