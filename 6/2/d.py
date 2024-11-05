# D. Лучший отдых

n, k = map(int, input().split())
a = map(int, input().split())
a = list(a)

ans = 0
a.sort()
l = r = 0
for l in range(n):
    while r < n and a[r] - a[l] <= k:
        r += 1
    ans = max(ans, r - l)

print(ans)
