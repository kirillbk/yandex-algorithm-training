# A. Равенство подстрок

P = 10**9 + 7
X = 257


def is_equal(
    a: int,
    b: int,
    l: int,
    h: list[int],
    x: list[int]
) -> bool:
    return (
        (h[a + l - 1] + h[b - 1] * x[l]) % P
        == (h[b + l - 1] + h[a - 1] * x[l]) % P
    )


s = input()
q = int(input())
"""
    h - хэш для всех подстрок строки s
    x - степени X
"""
n = len(s)
s = " " + s
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
for i in range(1, (n + 1)):
    h[i] = (h[i - 1] * X + ord(s[i])) % P
    x[i] = (x[i - 1] * X) % P

for _ in range(q):
    l, a, b = map(int, input().split())
    if is_equal(a + 1, b + 1, l, h, x):
        print("yes")
    else:
        print("no")
