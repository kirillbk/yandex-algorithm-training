# B. Одномерный морской бой
# https://oeis.org/A000292

n = int(input())
l = 0
r = n + 1
while r - l > 1:
    m = (l + r) // 2
    gaps = m * (m + 1) // 2 - 1
    cells = m * (m + 1) * (m + 2) // 6
    if gaps + cells <= n:
        l = m
    else:
        r = m

print(l)
