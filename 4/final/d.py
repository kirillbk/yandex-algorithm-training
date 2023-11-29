# D. Кирпичи

answer = []

def _solve(
        a: list[int],
        i: int,
        n: int,
        buffer: list[int],
    ):
    global answer

    if n == 0:
        if not answer or len(buffer) < len(answer):
            answer = buffer.copy()
        return
    if i == len(a) or n < 0 or (answer and len(buffer) > len(answer)):
        return

    buffer.append(a[i])
    buffer.append(a[i])
    _solve(a, i + 1, n - 2 * a[i], buffer)
    buffer.pop()
    _solve(a, i + 1, n - a[i], buffer)
    buffer.pop()
    _solve(a, i + 1, n, buffer)


def solution(a: list[int], n: int, m: int) -> list[int]:
    if 2 * sum(a) < n:
        return -1, []

    a = sorted(a, reverse=True)
    _solve(a, 0, n, [])

    return len(answer), answer


n, m = map(int, input().split())
a = list(map(int, input().split()))

k, bricks = solution(a, n, m)
print(k)
print(*bricks)
