# G. Разрушить казарму

from math import isinf


def solution(x, y, p) -> int:
    def no_barracks(x, a, round):
        while a > 0 and x > 0:
            a -= x
            x -= a
            round += 1

        if a > 0:
            return float('inf')
        return round

    answer = float('inf')
    rnd = 1
    a = 0
    while (a > 0 or y > 0) and x > 0:
        # cломать казарму в этом раунде, если это возможно
        if x >= y:
            r = no_barracks(2*x - (a + y), (a + y) - x, rnd)
            answer = min(answer, r)

        # убить всех солдат, нанести урон по казарме
        # eсли солдат <=, чем у противника (x <= a), а казарма не разрушена - победить с лучшим результатом не получится
        if x > a:
            y -= x - a
            a = 0
        elif y > 0:
            break

        if y > 0:
            a += p
        rnd += 1

    if a <= 0 and y <= 0:
        answer = min(answer, r)

    if isinf(answer):
        return -1
    return answer


x = int(input())
y = int(input())
p = int(input())

print(solution(x, y, p))
