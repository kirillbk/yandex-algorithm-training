# E. Подпалиндромы

def mahacher(s: str) -> list[int]:
    # чтобы не писать два алгоритма для чётных и нечётных палиндромов
    s = '#' + '#'.join(s) + '#'
    d = [1] * len(s)

    l = r = 0
    for i in range(0, len(s)):
        if i <= r:
            d[i] = min(r - i + 1, d[l + (r - i)])
        while i - d[i] >= 0 and i + d[i] < len(s) and s[i - d[i]] == s[i + d[i]]:
            d[i] += 1
        if i + d[i] - 1 > r:
            l = i - d[i] + 1
            r = i + d[i] - 1

    return d


d = mahacher(input())
answer = sum(map(lambda x: x // 2, d))
print(answer)

