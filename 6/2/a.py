# A. Префиксные суммы

n = int(input())
a = list(map(int, input().split()))

b = [0] * n
b[0] = a[0]
for i in range(1, n):
    b[i] = b[i - 1] + a[i]

print(*b)
