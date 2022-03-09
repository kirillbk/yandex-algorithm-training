n, i, j = map(int, input().split())

d = abs(j - i) - 1
print(min(d, n - d - 2))
