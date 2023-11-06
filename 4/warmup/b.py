# B. Сложить две дроби

from math import gcd


a, b, c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d
divider = gcd(numerator, denominator)
print(numerator // divider, denominator // divider)
