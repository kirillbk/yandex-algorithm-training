# F. Колесо Фортуны

n = int(input())
m = [*map(int, input().split())]
a, b, k = map(int, input().split())

r = (b - a) // k
if r < n:
    low = (a - 1) // k
    hi = (b - 1) // k
    answer = -1
    for i in range(low, hi + 1):
        j = i % n
        answer = max(answer, m[j])
        if j != 0:
            answer = max(answer, m[n - j])
    print(answer)
else:
    print(max(m))

