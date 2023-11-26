# A. Все перестановки заданной длины

def solution(n: int, used: list[bool], result: list[int]):
    if len(result) == n:
        print(*result, sep='')
        return

    for j in range(1, n + 1):
        if used[j]:
            continue

        result.append(j)
        used[j] = True
        solution(n, used, result)
        result.pop()
        used[j] = False


n = int(input())
solution(n, [False] * (n + 1), [])
