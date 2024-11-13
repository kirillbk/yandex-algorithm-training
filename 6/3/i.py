# I. Автоматизированный склад

from operator import itemgetter
from collections import deque


TIME = 0


def solution(n: int, a: int, b: int, rovers: list[tuple[int, int]]) -> list[int]:
    # сортировка всех роверов по времени прибытия
    tmp = ((rovers[i][0], rovers[i][1], i) for i in range(n))
    rovers = sorted(tmp, key=itemgetter(1))

    roads = [deque() for _ in range(5)]
    for dir, t, i in rovers:
        roads[dir].append((t, i))

    # a - часть главной дороги без помех справа, b - возможны помехи справа
    if a > b and not (a == 4 and b == 1) or a == 1 and b == 4:
        a, b = b, a
    # главная(и второстепенная) дорога поворачивает
    is_turn = b - a != 2

    ans = [0] * n
    cntr = 0
    time = 0
    while cntr < n:
        # есть ровер на дороге a
        if roads[a] and roads[a][0][TIME] <= time:
            _, no = roads[a].popleft()
            cntr += 1
            ans[no] = time
            # главная дорога прямая и есть ровер на дороге b
            if not is_turn and roads[b] and roads[b][0][TIME] <= time:
                _, no = roads[b].popleft()
                cntr += 1
                ans[no] = time
        # есть ровер на доргое b
        elif roads[b] and roads[b][0][TIME] <= time:
            _, no = roads[b].popleft()
            cntr += 1
            ans[no] = time
        # нет роверов на главной дороге, рассматриваем второстепенную
        else:
            for dir in range(1, 5):
                if dir == a or dir == b:
                    continue
                right = 4 if dir == 1 else dir - 1
                # есть ровер и нет помехи справа
                if (
                    roads[dir]
                    and roads[dir][0][TIME] <= time
                    and (not roads[right] or roads[right][0][TIME] > time)
                ):
                    _, no = roads[dir].popleft()
                    cntr += 1
                    ans[no] += time
                    # есть поворот на второстепенной дороге, может проехать только один ровер
                    if is_turn:
                        break
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
