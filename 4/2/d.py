# D. Кубики в зеркале

def hash(a: list[int], n: int) -> list[int]:
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * X + a[i - 1]) % P

    return h


n, m = map(int, input().split())
a = list(map(int, input().split()))

P = 10**9 + 7
X = m + 1

h1 = hash(a, n)
h2 = hash(a[::-1], n)
x = [0] * (n + 1)
x[0] = 1
for i in range(1, n + 1):
    x[i] = (x[i - 1] * X) % P

answer = []
for i in range(0, n // 2 + 1):
    if (
        (h1[i + i - 1] + h2[n - i - 1] * x[i]) % P
        == (h2[n - i + i - 1] + h1[i - 1] * x[i]) % P
    ):
        answer.append(n - i)

print(*reversed(answer))
