# D. Шахматная доска

n = int(input())

cells = set()
for _ in range(n):
    y, x = map(int, input().split())
    cells.add((y, x))

p = 0
steps = (0, 1), (0, -1), (1, 0), (-1, 0)
for y, x in cells:
    for dx, dy in steps:
        if (y + dy, x + dx) not in cells:
            p += 1

print(p)
