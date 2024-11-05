# J. Исследование улик


def solution(n: int, a: list[int], m: int, k: int, x: list[int]) -> list[int]:
    prefix = [0] * n
    limit = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            prefix[i] = prefix[i - 1]
        elif a[i] < a[i - 1]:
            prefix[i] = i
            limit = 0
        else:
            limit += 1
            l = prefix[i - 1]
            while limit > k:
                if a[l] == a[l + 1]:
                    limit -= 1
                l += 1
            prefix[i] = l

    ans = [0] * m
    for i in range(m):
        ans[i] = prefix[x[i] - 1] + 1

    return ans


n = int(input())
a = map(int, input().split())
a = list(a)
m, k = map(int, input().split())
x = map(int, input().split())
x = list(x)

ans = solution(n, a, m, k, x)
print(*ans)


# Тесты
ans = solution(6, [3, 3, 3, 4, 4, 5], 4, 2, [3, 4, 5, 6])
assert ans == [1, 1, 2, 2]

ans = solution(7, [1, 5, 7, 2, 10, 10, 6], 7, 0, [1, 2, 3, 4, 5, 6, 7])
assert ans == [1, 1, 1, 4, 4, 6, 7]

ans = solution(7, [3, 3, 3, 3, 2, 2, 2], 7, 2, [1, 2, 3, 4, 5, 6, 7])
assert ans == [1, 1, 1, 2, 5, 5, 5]

ans = solution(9, [3, 2, 2, 3, 4, 2, 5, 5, 2], 1, 1, [8])
assert ans == [6]

ans = solution(
    10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)
assert ans == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans = solution(4, [1, 3, 2, 3], 1, 0, [4])
assert ans == [3]

ans = solution(7, [1, 5, 7, 2, 10, 10, 6], 7, 0, [1, 2, 3, 4, 5, 6, 7])
assert ans == [1, 1, 1, 4, 4, 6, 7]
