# C. Город Че

n, r = map(int, input().split())
d = map(int, input().split())
d = list(d)

ans = 0
right = 0
for lelft in range(n):
    while right < n and d[right] - d[lelft] <= r:
        right += 1
    ans += n - right

print(ans)
