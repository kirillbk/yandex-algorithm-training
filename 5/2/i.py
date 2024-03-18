# I. Пираты Баренцева моря

n = int(input())
ships = []
for _ in range(n):
    y, x_ = map(int, input().split())
    ships.append((x_, y))

y_ships_cntr = [0] * (n + 1)
for _, y in ships:
    y_ships_cntr[y] += 1

alignment = 0
for y in range(1, n + 1):
    y_ = 1
    while y_ships_cntr[y] > 1:
        if y_ships_cntr[y_] == 0:
            y_ships_cntr[y] -= 1
            y_ships_cntr[y_] += 1
            alignment += abs(y - y_)
        y_ += 1

answer = float('inf')
for x in range(1, n + 1):
    steps = alignment
    for x_, _ in ships:
        steps += abs(x - x_)
    answer = min(answer, steps)

print(answer)
