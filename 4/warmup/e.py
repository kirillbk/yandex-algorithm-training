# E. Средний уровень

n = int(input())
a = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]
for i in range(n):
    low = a[i] * i - prefix[i]
    high = prefix[-1] - (prefix[i] + a[i]) - (n - i - 1) * a[i]
    print(low + high, end=' ')
