# I. Сапер
# Вам необходимо построить поле для игры "Сапер" по его конфигурации – размерам и координатам расставленных на нем мин.
# Вкратце напомним правила построения поля для игры "Сапер":
# Поле состоит из клеток с минами и пустых клеток
# Клетки с миной обозначаются символом *
# Пустые клетки содержат число ki,j, 0≤ ki, j ≤ 8 – количество мин на соседних клетках. Соседними клетками являются восемь клеток, имеющих смежный угол или сторону.

# Формат ввода
# В первой строке содержатся три числа: N, 1 ≤ N ≤ 100 - количество строк на поле, M, 1 ≤ M ≤ 100 - количество столбцов на поле, K, 0 ≤ K ≤ N ⋅ M - количество мин на поле.
# В следующих K строках содержатся по два числа с координатами мин: p, 1 ≤ p ≤ N - номер строки мины, q, 1 ≤ 1 ≤ M - номер столбца мины.

# Формат вывода
# Выведите построенное поле, разделяя строки поля переводом строки, а столбцы - пробелом.

n, m, k = map(int, input().split())
#поле на 2 клетки больше по m и n
area = [[0] * (m + 2) for _ in range(n + 2)]
for _ in range(k):
	p, q = map(int, input().split())
	area[p][q] = '*'
	# +1 к каждой клетке рядом с миной
	for i in range(p - 1, p + 2):
		for j in range(q - 1, q + 2):
			if area[i][j] != '*':
				area[i][j] += 1

for i in range(1, n + 1):
	print(*area[i][1:m + 1])