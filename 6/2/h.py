# H. Переезд в опенспейс

n = int(input())
a = map(int, input().split())
a = list(a)

# количество переходов в кабинет слева
prefix = [0] * n
total = a[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + total
    total += a[i]
# количество переходов в кабинет справа
suffix = [0] * n
total = a[-1]
for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] + total
    total += a[i]
# кабинет с минимальным количеством переходов
ans = prefix[0] + suffix[0]
for i in range(1, n):
    ans = min(ans, prefix[i] + suffix[i])

print(ans)
