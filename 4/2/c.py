# C. Z-функция

def z(s: str) -> list[int]:
    z = [0] * len(s)
    l = r = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


# поиск значения Z-функции с помощью бинпоиска и хэшей для строки (как в разборе)
def z_hash(s: str) -> list[int]:
    n = len(s)

    P = 10**9 + 7
    X = 257

    x = [0] * (n + 1)
    x[0] = 1
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * X + ord(s[i - 1])) % P
        x[i] = (x[i - 1] * X) % P

    z = [0] * n
    for i in range(1, n):
        l = 0
        r = n - i + 1
        while r - l > 1:
            m = (r + l) // 2
            if (
                (h[m] + h[i] * x[m]) % P
                == (h[i + m] + h[0] * x[m]) % P
            ):
                l = m
            else:
                r = m
        z[i] = l

    return z


s = input()
print(*z_hash(s))
