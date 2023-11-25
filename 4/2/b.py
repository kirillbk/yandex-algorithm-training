# B. Основание строки

P = 10**9 + 7
X = 257


def is_equal(
    a: int,
    b: int,
    l: int
) -> bool:
    return (
        (h[a + l - 1] + h[b - 1] * x[l]) % P
        == (h[b + l - 1] + h[a - 1] * x[l]) % P
    )


s = input()

n = len(s)
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
for i in range(1, n + 1):
    h[i] = ((h[i - 1] * X) + ord(s[i - 1])) % P
    x[i] = (x[i - 1] * X) % P

for k in range(1, n + 1):
    if is_equal(1, k + 1, n - k):
        print(k)
        break
