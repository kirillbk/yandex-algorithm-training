IN = 1
OUT = -1

n = int(input())
events = list()
for i in range(n):
	t, l = map(int, input().split())
	events.append((t, IN))
	events.append((t + l, OUT))

events.sort()
now = 0
answer = 0
for _, event in events:
	if event == IN:
		now += 1
	else:
		now -= 1
	answer = max(now, answer)

print(answer)
