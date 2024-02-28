# C. Минимальное покрытие

m = int(input())
lines = []
while True:
    l, r = map(int, input().split())
    if l == r == 0:
        break
    if r > 0 and l < m:
        lines.append((l, r))

lines.sort()
answer = []
right_covered = 0
line = 0, 0
for l, r in lines:
    if l > right_covered:
        answer.append(line)
        right_covered = line[1]
        if right_covered >= m:
            break
    if l <= right_covered and r > line[1]:
        line = l, r
if right_covered < m:
    answer.append(line)
    right_covered = line[1]

if right_covered < m:
    print('No solution')
else:
    print(len(answer))
    for line in answer:
        print(*line)
