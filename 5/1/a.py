# A. Покраска деревьев

p, v = map(int, input().split())
q, m = map(int, input().split())

a0, a1 = p - v, p + v
b0, b1 = q - m, q + m
if b0 <= a1 and b1 >= a0:
    x0 = min(a0, b0)
    x1 = max(a1, b1)
    print(x1 - x0 + 1)
else:
    print((a1 - a0 + 1) + (b1 - b0 + 1))

