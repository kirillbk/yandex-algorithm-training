# I. Изучение алгоритмов

from collections.abc import Iterable


def solution(a: Iterable[int], b: Iterable[int], p: Iterable[int], n: int) -> list[int]:
    a_ = list(enumerate(a))
    b_ = list(enumerate(b))
    p = list(p)

    a = sorted(a_, key=lambda x: (x[1], b_[x[0]][1], -x[0]), reverse=True)
    b = sorted(b_, key=lambda x: (x[1], a_[x[0]][1], -x[0]), reverse=True)

    ans = [0] * n
    i = j = 0
    learned = [False] * (n + 1)
    for k in range(n):
        while i < n and learned[a[i][0]]:
            i += 1
        while j < n and learned[b[j][0]]:
            j += 1
        if i < n and (p[k] == 0 or j == n):
            no, _ = a[i]
            i += 1
        else:
            no, _ = b[j]
            j += 1
        learned[no] = True
        ans[k] = no + 1

    return ans


n = int(input())
a = map(int, input().split())
b = map(int, input().split())
p = map(int, input().split())

print(*solution(a, b, p, n))


# Тесты
n = 5
a = 1, 2, 3, 4, 5
b = 5, 4, 3, 2, 1
p = 1, 0, 1, 0, 0
assert solution(a, b, p, n) == [1, 5, 2, 4, 3]

n = 6
a = 3, 10, 6, 2, 10, 1
b = 3, 5, 10, 7, 5, 9
p = 0, 0, 1, 1, 0, 1
assert solution(a, b, p, n) == [2, 5, 3, 6, 1, 4]

n = 5
a = 5, 5, 5, 5, 5
b = 1, 2, 3, 4, 5
p = 0, 0, 0, 0, 0
assert solution(a, b, p, n) == [5, 4, 3, 2, 1]

n = 5
a = 5, 5, 5, 5, 5
b = 5, 4, 3, 2, 1
p = 1, 1, 1, 1, 1
assert solution(a, b, p, n) == [1, 2, 3, 4, 5]

n = 5
a = 1, 2, 3, 4, 5
b = 5, 4, 3, 2, 1
p = 0, 0, 0, 0, 0
assert solution(a, b, p, n) == [5, 4, 3, 2, 1]

n = 5
a = 1, 2, 3, 4, 5
b = 5, 4, 3, 2, 1
p = 1, 1, 1, 1, 1
assert solution(a, b, p, n) == [1, 2, 3, 4, 5]

n = 5
a = 10, 10, 20, 20, 10
b = 20, 10, 20, 10, 20
p = 0, 0, 0, 1, 1
assert solution(a, b, p, n) == [3, 4, 1, 5, 2]

n = 5
a = 5, 5, 5, 5, 5
b = 5, 5, 5, 5, 5
p = 1, 0, 1, 0, 0
assert solution(a, b, p, n) == [1, 2, 3, 4, 5]

n = 5
a = 1, 1, 1, 1, 2
b = 1, 1, 1, 1, 1
p = 1, 0, 1, 0, 0
assert solution(a, b, p, n) == [5, 1, 2, 3, 4]

n = 5
a = 1, 2, 3, 4, 5
b = 5, 4, 3, 2, 1
p = 1, 0, 1, 0, 0
assert solution(a, b, p, n) == [1, 5, 2, 4, 3]

n = 6
a = 3, 10, 6, 2, 10, 1
b = 3, 5, 10, 7, 5, 9
p = 0, 0, 1, 1, 0, 1
assert solution(a, b, p, n) == [2, 5, 3, 6, 1, 4]
