# G. Построить квадрат

def solution(points: list[tuple[int, int]], n: int) -> int:
    first_p = points[0]
    # в худшем случае придётся добавить 3 точки
    answer = (
        (first_p[0] + 1, first_p[1]),
        (first_p[0], first_p[1] + 1),
        (first_p[0] + 1, first_p[1] + 1),
    )
    points_set = set(points)

    for a in range(n - 1):
        for b in range(a + 1, n):
            ax, ay = points[a]
            bx, by = points[b]
            # предположим, что точки a и b лежат на диагонали квадрата
            # вектор v, перпендикулярный диагонали квадрата
            vx = -by + ay
            vy = bx - ax

            # координаты точек c и d должны быть целыми числами
            x = (bx + ax + vx)
            cx = x // 2
            y = (by + ay + vy)
            cy = y // 2
            if x % 2 or y % 2:
                continue

            x = (bx + ax - vx)
            dx =  x // 2
            y = (by + ay - vy)
            dy = y // 2
            if x % 2 or y % 2:
                continue

            c = cx, cy
            d = dx, dy
            c_exists = c in points_set
            d_exists = d in points_set
            if c_exists and d_exists:
                return ()
            elif c_exists:
                answer = d,
            elif d_exists:
                answer = c,
            elif len(answer) > 2:
                answer = c, d

    return answer


n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

answer = solution(points, n)

print(len(answer))
for p in answer:
    print(*p)
