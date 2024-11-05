# B. Майки и носки

a = int(input())
b = int(input())
c = int(input())
d = int(input())

ans = []
if a > 0 and c > 0:
    ans.append((b + 1, d + 1))
if b > 0 and d > 0:
    ans.append((a + 1, c + 1))
if a > 0 and b > 0:
    ans.append((max(a, b) + 1, 1))
if c > 0 and d > 0:
    ans.append((1, max(c, d) + 1))

print(*min(ans, key=sum))
