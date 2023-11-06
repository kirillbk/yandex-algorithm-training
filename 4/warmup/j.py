# J. Групповой проект

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())

    gropus = n // a
    if n % a <= (b - a) * gropus:
        print('YES')
    else:
        print('NO')
