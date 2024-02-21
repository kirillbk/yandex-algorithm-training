# E. Царь Леонид на тракторе

from collections import deque
from math import isinf


def bfs01(field: list[str], h, w, sx, sy, tx, ty) -> int:
    sx -= 1
    sy = h - sy
    tx -= 1
    ty = h - ty

    directions = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    turns = [[[float('inf')] * len(directions) for _ in range(w)] for _ in range(h)]
    q = deque()

    for dir in range(len(directions)):
        q.append((sx, sy, dir))
        turns[sy][sx][dir] = 1

    while q:
        x, y, dir = q.popleft()

        if x == tx and y == ty:
            break

        for to_dir in range(len(directions)):
            dx, dy = directions[to_dir]
            to_x = x + dx
            to_y = y + dy

            if to_x < 0 or to_x >= w or to_y < 0 or to_y >= h:
                continue
            if field[to_y][to_x] == 'X':
                continue

            if to_dir == dir and turns[y][x][dir] < turns[to_y][to_x][to_dir]:
                turns[to_y][to_x][to_dir] = turns[y][x][to_dir]
                q.appendleft((to_x, to_y, to_dir))
            elif turns[y][x][dir] + 1 < turns[to_y][to_x][to_dir]:
                turns[to_y][to_x][to_dir] = turns[y][x][dir] + 1
                q.append((to_x, to_y, to_dir))

    answer = min(turns[ty][tx])
    if isinf(answer):
        return -1
    return answer


h, w = map(int, input().split())
field = [input() for _ in range(h)]
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

print(bfs01(field, h, w, sx, sy, tx, ty))
