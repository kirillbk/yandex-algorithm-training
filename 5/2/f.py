# F. Колесо Фортуны

n = int(input())
m = [*map(int, input().split())]
a, b, k = map(int, input().split())

c = b - a + 1
r = c // k - (0 if c % k else 1)
if r < n:
    low = a // k - (0 if a % k else 1)
    left = low % n
    answer = -1
    for i in range(left, left + r + 1):
        j = i % n
        answer = max(answer, m[j])
        if j != 0:
            answer = max(answer, m[n - j])
    print(answer)
else:
    print(max(m))

