# E. Удаление медиан

n = int(input())
a = map(int, input().split())
a = list(a)

a.sort()
ans = []
m = n // 2
l = m - 1
if n % 2:
    ans.append(a[m])
    r = m + 1
else:
    r = m
while l > -1 or r < n:
    l_len = l + 1
    r_len = n - r
    if l > -1 and (l_len > r_len or (l_len == r_len and a[l] <= a[r])):
        ans.append(a[l])
        l -= 1
    else:
        ans.append(a[r])
        r += 1

print(*ans)
