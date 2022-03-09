# E. Пирамида
# Для строительство двухмерной пирамиды используются прямоугольные блоки, каждый из которых характеризуется шириной и высотой. Можно поставить один блок на другой, только если ширина верхнего блока строго меньше ширины нижнего. Самым нижним в пирамиде может быть блок любой ширины.
# По заданному набору блоков определите, пирамиду какой наибольшей высоты можно построить из них.

# Формат ввода
# В первой строке входных данных задается число 
# N — количество блоков (1≤N≤100000). В следующий N строках задаются пары натуральных чисел wi и hi (1≤wi,hi≤109) — ширина и высота блока соответственно.

# Формат вывода
# Выведите одно целое число — максимальную высоту пирамиды.

n = int(input())
blocks = dict()
for _ in range(n):
	w, h = map(int, input().split())
	if w in blocks and h > blocks[w] or w not in blocks:
		blocks[w] = h

print(sum(blocks.values()))