# B. Через тернии к клиенту

from collections import defaultdict


n = int(input())
events = []
for _ in range(n):
    data, s = input().rsplit(maxsplit=1)
    d, h, m, id = map(int, data.split())
    time = m + h * 60 + d * 24 * 60
    if s != 'B':
        events.append((time, id, s))

events.sort()
answer = defaultdict(int)
start_time = dict()
for time, id, s in events:
    if s == 'A':
        start_time[id] = time
    else:
        answer[id] += time - start_time[id]

print(*(time for _, time in sorted(answer.items())))
