# 38. Блохи

from collections import deque

def bfs(field, start_y, start_x):
	dx = 1, 1, 2, 2, -1, -1, -2, -2
	dy = 2, -2, 1, -1, 2, -2, 1, -1
	q = deque()

	field[start_y][start_x] = 0
	q.append((start_y, start_x))
	while q:
		now_y, now_x  = q.popleft()
		for i in range(8):
			to_x = now_x + dx[i]
			to_y = now_y + dy[i]
			if field[to_y][to_x] == -1:
				field[to_y][to_x] = field[now_y][now_x] + 1
				q.append((to_y, to_x))


n, m, s, t, q = map(int, input().split())
fleas = list()
for _ in range(q):
	x, y = map(int, input().split())
	fleas.append((x, y))

field = [[-1] * (m + 3) for _ in range(n + 3)]
for i in range(n + 3):
	field[i][0] = 0
	field[i][m+1] = 0
	field[i][m+2] = 0
for j in range(m + 3):
	field[0][j] = 0
	field[n+1][j] = 0
	field[n+2][j] = 0
bfs(field, s, t)

answer = 0
for y, x in fleas:
	if field[y][x] == -1:
		answer = -1
		break
	else:
		answer += field[y][x]
print(answer)
