# J. Кровать из стульев

from collections.abc import Iterable
from collections import deque


def solution(n: int, height: int, h: Iterable[int], w: Iterable[int]) -> int:
    chairs = sorted(zip(h, w))

    ans = float("inf")
    d = deque((0,))
    length = chairs[0][1]
    r = 1
    for l in range(n):
        while r < n and length < height:
            diff = abs(chairs[r][0] - chairs[r - 1][0])
            while d and d[-1] < diff:
                d.pop()
            d.append(diff)
            length += chairs[r][1]
            r += 1

        if length >= height:
            ans = min(ans, d[0])

        length -= chairs[l][1]
        if r - l <= 2:
            d = deque((0,))
        elif d[0] == abs(chairs[l][0] - chairs[l + 1][0]):
            d.popleft()

    return ans


n, height = map(int, input().split())
h = map(int, input().split())
w = map(int, input().split())

print(solution(n, height, h, w))
