n = int(input())
events = list()
for i in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))
    events.append((r, -1))

events.sort()
now = 0
answer = 0
for i in range(len(events)):
    if now > 0:
        answer += events[i][0] - events[i - 1][0]
    if events[i][1] == 1:
        now += 1
    else:
        now -= 1

print(answer)
