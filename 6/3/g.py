# G. Очередь в ПВЗ


def solution(n: int, b: int, a: list[int]) -> int:
    ans = 0
    queue = 0
    for i in range(n):
        queue += a[i]
        ans += queue
        if queue > b:
            queue -= b
        else:
            queue = 0
    ans += queue

    return ans


n, b = map(int, input().split())
a = list(map(int, input().split()))

print(solution(n, b, a))
