# A. Быстрый поиск в массиве

def lbs(a: list[int], x: int) -> int:
    l = -1
    r = len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] >= x:
            r = m
        else:
            l = m
    return r


def rbs(a: list[int], x: int) -> int:
    l = -1
    r = len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return l


n = int(input())
a = [*map(int, input().split())]
k = int(input())

a.sort()
answer = []
for _ in range(k):
    l, r = map(int, input().split())
    greater = lbs(a, l)
    less = rbs(a, r)
    if less < greater:
        answer.append(0)
    else:
        answer.append((less - greater + 1))

print(*answer)
