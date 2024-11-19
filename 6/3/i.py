# I. Автоматизированный склад

from collections import deque
from collections.abc import Iterable
from operator import itemgetter


def solution(n: int, a: int, b: int, rovers: Iterable[tuple[int, int]]) -> list[int]:
    # сортировка всех роверов по времени прибытия
    tmp = ((rovers[i][0], rovers[i][1], i) for i in range(n))
    rovers = sorted(tmp, key=itemgetter(1))

    roads = [deque() for _ in range(4)]
    for dir, t, i in rovers:
        roads[dir - 1].append((t, i))

    a -= 1
    b -= 1

    is_ready = lambda dir: roads[dir] and roads[dir][0][0] <= time
    is_main = lambda dir: dir == a or dir == b
    right = lambda dir: (dir - 1) % 4

    ans = [0] * n
    time = 1
    while n > 0:
        moves = [False] * 4

        for dir in range(4):
            if not is_ready(dir):
                continue
            # ровер на главной дороге и на главной дороге справа есть помеха
            if is_main(dir) and is_main(right(dir)) and is_ready(right(dir)):
                continue
            # ровер на второстепенной дороге и есть ровер на главной дороге или справа
            if not is_main(dir) and (
                is_ready(a) or is_ready(b) or is_ready(right(dir))
            ):
                continue
            moves[dir] = True

        for dir in range(4):
            if moves[dir]:
                _, no = roads[dir].popleft()
                ans[no] = time
                n -= 1

        time += 1

    return ans


n = int(input())
a, b = map(int, input().split())
rovers = []
for _ in range(n):
    d, t = map(int, input().split())
    rovers.append((d, t))

print(*solution(n, a, b, rovers), sep="\n")


# Тесты
# with open("test_i.txt") as f:
#     while True:
#         n = int(f.readline())
#         a, b = map(int, f.readline().split())
#         rovers = []
#         for _ in range(n):
#             d, t = map(int, f.readline().split())
#             rovers.append((d, t))

#         answer = list(map(int, f.readline().split()))
#         s = solution(n, a, b, rovers)
#         if answer != s:
#             print(f"answer  : {answer}")
#             print(f"solution: {s}")
#             break

#         if not f.readline():
#             break
