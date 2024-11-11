# C. Минимум на отрезке

from collections import deque


n, k = map(int, input().split())
a = map(int, input().split())
a = list(a)

d = deque()
for i in range(k):
    while d and d[-1] > a[i]:
        d.pop()
    d.append(a[i])
ans = [d[0]]
for i in range(k, n):
    while d and d[-1] > a[i]:
        d.pop()
    d.append(a[i])
    if d[0] == a[i - k]:
        d.popleft()
    ans.append(d[0])

print(*ans, sep="\n")
