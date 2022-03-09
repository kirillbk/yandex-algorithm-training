# B. Точки и отрезки
# Дано n отрезков на числовой прямой и m точек на этой же прямой. Для каждой из данных точек определите, скольким отрезкам они принадлежат. Точка x считается принадлежащей отрезку с концами a и b, если выполняется двойное неравенство min(a, b) ≤ x ≤ max(a, b).

# Формат ввода
# Первая строка содержит два целых числа n (1 ≤ n ≤ 10^5) – число отрезков и m (1 ≤ m ≤ 10^5) – число точек.
# В следующих n строках по два целых числи ai и bi – координаты концов соответствующего отрезка. 
# В последней строке m целых чисел – координаты точек. Все числа по модулю не превосходят 10^9

# Формат вывода
# В выходной файл выведите m чисел – для каждой точки количество отрезков, в которых она содержится.

import enum

class type(enum.IntEnum):
	begin = 1
	point = 2
	end = 3

n, m = map(int, input().split())
positions = []
for _ in range(n):
	begin, end = map(int, input().split())
	if begin > end:
		begin, end = end, begin
	positions.append((begin, type.begin))
	positions.append((end, type.end))
points = list(map(int, input().split()))
for i in range(m):
	positions.append((points[i], type.point, i))

positions.sort()
total = 0
result = [None] * m
for point in positions:
	if point[1] == type.begin:
		total += 1
	elif point[1] == type.end:
		total -= 1
	else:
		result[point[2]] = total

print(*result)
