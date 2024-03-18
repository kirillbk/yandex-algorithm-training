# G. Ни больше ни меньше

t = int(input())
for _ in range(t):
    n = int(input())
    a = [*map(int, input().split())]

    answer = []
    size = 1
    m = a[0]
    start = 0

    for i in range(1, n):
        size += 1
        if a[i] < size or m < size:
            answer.append(i - start)
            size = 1
            m = a[i]
            start = i
        else:
            m = min(m, a[i])
    answer.append(n - start)

    print(len(answer))
    print(*answer)
