# B. Зеркальная z-функция

P = 10**9 + 7
X = 257


def hash(s: str, n: int) -> list[int]:
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * X + ord(s[i - 1])) % P

    return h


n = int(input())
s = input()

h1 = hash(s, n)
h2 = hash(s[::-1], n)
x = [0] * (n + 1)
x[0] = 1
for i in range(1, n + 1):
    x[i] = (x[i - 1] * X) % P

z = [0] * n
for i in range(n):
    l = 0
    r = i + 1 + 1
    while r - l > 1:
        m = (r + l) // 2
        if (
            (h1[m] + h2[n - i - 1] * x[m]) % P
            == (h2[n - i + m - 1] + h1[0] * x[m]) % P
        ):
            l = m
        else:
            r = m
    z[i] = l

print(*z)
