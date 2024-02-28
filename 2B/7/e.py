# E. Полярные прямоугольники

from enum import IntEnum
from math import pi


Event = IntEnum('Event', 'BEGIN END')

r_min = -1
r_max = float('inf')
n = int(input())
events = []
for i in range(n):
    r1, r2, a1, a2 = map(float, input().split())
    r_min = max(r_min, r1)
    r_max = min(r_max, r2)
    events.append((a1, Event.BEGIN, i))
    events.append((a2, Event.END, i))

events.sort()
cntr = 0
active = set()
for _, event, i in events:
    if event == Event.BEGIN:
        active.add(i)
        cntr += 1
    elif i in active:
        cntr -= 1

answer = 0
for i in range(len(events) - 1):
    a, event, _ = events[i]
    if event == Event.BEGIN:
        cntr += 1
    else:
        cntr -= 1
    if cntr == n:
        angle = events[i + 1][0] - a
        answer += (r_max**2 - r_min**2) * angle / 2
a, event, _ =  events[-1]
if event == Event.BEGIN and cntr + 1 == n:
        angle = events[0][0] + (2 * pi - a)
        answer += (r_max**2 - r_min**2) * angle / 2

print(answer)
