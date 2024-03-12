# H. Забег по стадиону

from math import isinf


def solution(L: int, x1: int, v1: int, x2: int, v2: int) -> float:
    if x1 == x2 or x1 == L - x2 or x2 == L - x1:
        return 0.0
    if v1 == v2 == 0:
        return float('inf')
    if v1 == v2:
        s = min(x1, x2) + abs(x2 - x1) / 2
        if v1 > 0:
            s = L - s
        if s > L / 2:
            s -= L / 2
        return s / abs(v1)
    if abs(v1) == abs(v2):
        s = abs(x2 - x1)
        if x2 > x1 and v2 > v1 or x2 < x1 and v2 < v1:
            s = L - s
        return s / abs(v1) / 2

    if v1 < 0 and v2 > 0:
        t1 = (x2 + x1) / (-v1 - v2)
        if t1 < 0:
            t1 += L / abs(-v1 - v2)

        t2 = (-x1 + x2 + L) / (v1 - v2)
        if t2 < 0:
            t2 += L / abs(v1 - v2)

        t3 = (x1 - x2 + L) / (-v1 + v2)
        if t3 < 0:
            t3 += L / abs(-v1 + v2)
    elif v1 > 0 and v2 < 0:
        t1 = (-x1 - x2) / (v1 + v2)
        if t1 < 0:
            t1 += L / abs(v1 + v2)

        t2 = (x1 - x2 - L) / (-v1 + v2)
        if t2 < 0:
            t2 += L / abs(-v1 + v2)

        t3 = (-x1 + x2 - L) / (v1 - v2)
        if t3 < 0:
            t3 += L / abs(v1 - v2)
    else:
        t1 = (-x1 + x2) / (v1 - v2)
        if t1 < 0:
            t1 += L / abs(v1 - v2)

        t2 = (x1 + x2 - L) / (-v1 - v2)
        if t2 < 0:
            t2 += L / abs(-v1 - v2)

        t3 = (-x1 - x2 + L) / (v1 + v2)
        if t3 < 0:
            t3 += L / abs(v1 + v2)

    if t1 < 0: t1 = float('inf')
    if t2 < 0: t2 = float('inf')
    if t3 < 0: t3 = float('inf')

    return min(t1, t2, t3)


L, x1, v1, x2, v2 = map(int, input().split())

answer = solution(L, x1, v1, x2, v2)
if isinf(answer):
    print('NO')
else:
    print('YES')
    print(answer)

