# D. Наполненность котятами

LEFT = 0
KITTEN = 1
RIGHT = 2

n, m = map(int, input().split())
events = [(a, KITTEN, None) for a in map(int, input().split())]
for i in range(m):
    l, r = map(int, input().split())
    events.append((l, LEFT, i))
    events.append((r, RIGHT, i))

events.sort()
answer = [0] * m
kittens = 0
for _, event, i in events:
    if event == LEFT:
        answer[i] -= kittens
    elif event == RIGHT:
        answer[i] += kittens
    if event == KITTEN:
        kittens += 1

print(*answer)
