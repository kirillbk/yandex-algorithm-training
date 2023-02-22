# 16. Минимум на отрезке

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

answer = list()
d = deque()

for i in range(k):
	while d and d[-1] > a[i]:
		d.pop()
	d.append(a[i])
answer.append(d[0])

for i in range(1, n - k + 1):
	while d and d[-1] > a[i+k-1]:
		d.pop()
	d.append(a[i+k-1])
	if d and d[0] == a[i-1]:
		d.popleft()
	answer.append(d[0])

print(*answer)
