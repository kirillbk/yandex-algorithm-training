# E. Нумерация дробей

n = int(input())

l = 0
r = n
while r - l > 1:
    m = (l + r) // 2
    if m * (m + 1) // 2 >= n:
        r = m
    else:
        l = m

diagonal = r
pos = n - l * (l + 1) // 2
a = diagonal - pos + 1
b = pos
if diagonal % 2:
    a, b = b, a

print(f'{a}/{b}')
