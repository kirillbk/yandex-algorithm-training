# D. Круглая кровать

from math import hypot


# True, если не смогли пройти от левой до правой стены
def check_diameter(d: int, graph: list[int], n: int) -> bool:
    def dfs(v: int, visited: list[bool]):
        visited[v] = True
        for to in range(n + 2):
            if  not visited[to] and graph[v][to] != 0 and graph[v][to] < d:
                dfs(to, visited)

    visited = [False] * (n + 2)
    dfs(n, visited)

    return not visited[n + 1]


x_l, x_r = map(int, input().split())
r = int(input())
n = int(input())
palms = [] * n
for _ in range(n):
    x, y = map(int, input().split())
    palms.append((x, y))

# граф в виде матрицы смежности
# левая стена -> все пальмы, все пальмы -> правая стена, рёбра между всеми пальмами
graph = [[0] * (n + 2) for _ in range(n + 2)]
left_wall = n
right_wall = n + 1
for i in range(n):
    x, y = palms[i]
    for j in range(i):
        distance = hypot(x - palms[j][0], y - palms[j][1])
        graph[i][j] = graph[j][i] = distance - 2 * r
    graph[left_wall][i] = x - x_l - r
    graph[i][right_wall] = x_r - x - r

# бин поиск диаметра кровати от 0 до ширины комнаты
d_left = 0
d_right = x_r - x_l
for _ in range(30):
    d_middle = (d_left + d_right) / 2
    if check_diameter(d_middle, graph, n):
        d_left = d_middle
    else:
        d_right = d_middle

if d_left == 0:
    print(0)
else:
    print(f'{d_left:.03f}')
